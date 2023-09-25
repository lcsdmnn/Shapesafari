import bpy


class SHAPESAFARI_OT_eraser(bpy.types.Operator):
    """Erase something"""
    bl_idname = "shapesafari.eraser_operator"
    bl_label = "Eraser Tool"



    @classmethod
    def poll(cls, context):
        return context.object is not None

    def invoke(self, context, event):
        scene = context.scene
        obj = context.active_object
        bpy.ops.sculpt.sculptmode_toggle()
        context.window_manager.modal_handler_add(self)

        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        if event.type == "LEFTMOUSE":
            bpy.ops.sculpt.trim_box_gesture("INVOKE_DEFAULT")


        if event.type in ('ESC', "RIGHTMOUSE", "RET"):
            bpy.ops.object.mode_set(mode='OBJECT')
            return {'FINISHED'}

        return {"RUNNING_MODAL"}