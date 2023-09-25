import bpy
import numpy as np
import cv2


def setScene(context):
    bpy.context.preferences.inputs.use_mouse_depth_navigate = True
    bpy.context.preferences.inputs.use_auto_perspective = False
    bpy.context.preferences.inputs.use_rotate_around_active = True
    bpy.context.preferences.inputs.use_zoom_to_mouse = True
    bpy.context.space_data.show_gizmo_navigate = False

    for a in bpy.context.screen.areas:
        if a.type == 'VIEW_3D':
            for s in a.spaces:
                if s.type == 'VIEW_3D':
                    s.lens = 250
                    s.clip_start = 1
                    s.clip_end = 100000


def ordering(pts):
    rectangular = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=2)
    rectangular[0] = pts[np.argmin(s)]
    rectangular[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=2)
    rectangular[1] = pts[np.argmin(diff)]
    rectangular[3] = pts[np.argmax(diff)]

    return rectangular


def transform_points(pts):
    rect = ordering(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    distorted = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, distorted)

    return M, maxHeight, maxWidth


def outer_contour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
            length = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.015 * length, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest


class Matrix:
    matrix = None
    maxHeight = None
    maxWidth = None


class SHAPESAFARI_OT_calibrate(bpy.types.Operator):
    bl_idname = "shapesafari.calibrate_operator"
    bl_label = "Calibrate"
    def execute(self, context):


        setScene(context)

        cap = cv2.VideoCapture(1)
        ret, img = cap.read()


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 20, 30, 30)
        edged = cv2.Canny(gray, 10, 20)


        contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        biggest = outer_contour(contours)
        Matrix.matrix, Matrix.maxHeight, Matrix.maxWidth = transform_points(biggest)
        print("CALIBRATE:",Matrix.matrix,Matrix.maxWidth,Matrix.maxHeight)


        return {"FINISHED"}



