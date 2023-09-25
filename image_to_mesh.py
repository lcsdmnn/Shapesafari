import bpy
import cv2
import numpy as np
import mathutils
import math
import bmesh

from .calibrate import Matrix

def getArea(context):

    for a in bpy.context.screen.areas:
        if a.type == 'VIEW_3D':
            area = a
            for r in a.regions:
                if r.type == 'WINDOW':
                    vp_width = r.width
                    vp_height = r.height
    return area, vp_width, vp_height



def contour(image):

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    approx_contours = [cv2.approxPolyDP(cnt, 0.002 * cv2.arcLength(cnt, True), True) for cnt in contours]


    return approx_contours


def getHelperFrame(img_width, img_height):

    outerFrame  = np.array([[         0,              0],
                            [ img_width,              0],
                            [ img_width, img_height * 1],
                            [         0, img_height * 1]], dtype="int32")


    innerFrame = np.array([[         0 +1,                0 +1],
                           [ img_width -1,                0 +1],
                           [ img_width -1, (img_height * 1) -1],
                           [         0 +1, (img_height * 1) -1]], dtype="int32")

    return outerFrame, innerFrame


class SHAPESAFARI_OT_image_to_mesh(bpy.types.Operator):
    bl_idname = "shapesafari.imagetomesh_operator"
    bl_label = "Image to Mesh"

    def execute(self, context):


        area, vp_width, vp_height = getArea(context)

        location = area.spaces[0].region_3d.view_location
        rotation = area.spaces[0].region_3d.view_rotation
        distance = area.spaces[0].region_3d.view_distance

        rotMatrix = mathutils.Quaternion.to_matrix(rotation)
        testVector = mathutils.Vector((0.0, 0.0, 1.0))
        testVector.rotate(rotation)


        cap = cv2.VideoCapture(1)
        ret, image = cap.read()
        cap.release()

        warped = cv2.warpPerspective(image, Matrix.matrix, (Matrix.maxWidth, Matrix.maxHeight))
        height = warped.shape[0]
        width = warped.shape[1]
        relation = width // height
        cut_width = 10
        cut_height = cut_width * relation
        new_height = (height - (cut_height//2))
        new_width = (width - (cut_width//2))

        warped = warped[(cut_height//2):new_height, (cut_width//2):new_width]
        approx_contours = contour(warped)

        index = 0
        for i in approx_contours:
            if len(i) <= 3:
                approx_contours.pop(index)
            else:
                pass
            index = index + 1


        img_height = warped.shape[0]
        img_width = warped.shape[1]

        outerFrame, innerFrame = getHelperFrame(img_width, img_height)
        approx_contours.append(outerFrame)
        approx_contours.append(innerFrame)

        vertices = np.array([], dtype="int32")
        for i in approx_contours:
            vertices = np.append(vertices, i)
        c = np.reshape(vertices, (-1, 2))


        verteciesList = np.array([], dtype="int32")
        for b in c:

            vertex = np.append(b, 0)
            verteciesList = np.append(verteciesList, vertex)
        d = np.reshape(verteciesList, (-1, 3))

        finalVertices = np.reshape(d, (-1, 3))


        liste = []
        counter = 0
        counter2 = 0
        street_complete = np.array([], dtype=int)
        for i in approx_contours:

            counter = counter + len(i)
            liste.append(counter)
            street2 = np.arange(counter2, counter, 1, dtype=int)

            counter2 = counter
            copy = street2.copy()
            rolled = np.roll(copy, 1)

            stacked = np.vstack((street2, rolled))

            rotated = np.rot90(stacked, axes=(1, 0))
            street_complete = np.append(street_complete, rotated)

        finalEdges = np.reshape(street_complete, (-1, 2))


        mesh = bpy.data.meshes.new("Surface")
        mesh.from_pydata(finalVertices, finalEdges, [])
        mesh.validate()
        obj = bpy.data.objects.new("Surface", mesh)
        bpy.context.scene.collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj

        bpy.ops.object.editmode_toggle(True)
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        # mirror
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0.0, 0.0, 0.0),
                         matrix=mathutils.Matrix.Rotation(math.radians(180.0), 3, 'X'))

        correctVector = ((img_width * -0.5), img_height * 0.5, 0)
        bmesh.ops.translate(bm, vec=correctVector, verts=bm.verts)

        # scale
        bmesh.ops.scale(bm, vec=(0.0165, 0.0165, 0.0165), verts=bm.verts)

        # rotate
        bmesh.ops.rotate(bm, matrix=rotMatrix, verts=bm.verts)

        # move to the point that is being looked at
        bmesh.ops.translate(bm, vec=(location), verts=bm.verts)

        # move to camera

        bmesh.ops.translate(bm, vec=testVector * (distance - 29), verts=bm.verts)
        bmesh.ops.triangle_fill(bm, edges=bm.edges)

        # Here the helper frame is deleted. It is no longer needed.
        bmesh.ops.delete(bm, geom=bm.verts[-8:])
        bmesh.update_edit_mesh(me)
        bpy.ops.object.editmode_toggle(True)

        print("IMAGE:", Matrix.matrix, Matrix.maxWidth, Matrix.maxHeight)

        return {"FINISHED"}