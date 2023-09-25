import bpy


class SHAPESAFAFARI_OT_loft(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "shapesafari.loft_operator"
    bl_label = "Loft Tool"


    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        scene = context.scene

        obj = context.selected_objects
        bpy.ops.object.join()

        bpy.ops.object.editmode_toggle()

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.bridge_edge_loops()
        bpy.ops.object.editmode_toggle()

        return {'CANCELLED'}
