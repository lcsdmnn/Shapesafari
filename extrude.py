import bpy


class SHAPESAFARI_OT_extrude(bpy.types.Operator):
    """Extrude a surface along its face normal"""
    bl_idname = "shapesafari.extrude_operator"
    bl_label = "Extrude Tool"


    @classmethod
    def poll(cls, context):
        return context.object is not None

    def modal(self, context, event):
        if event.type == 'WHEELUPMOUSE':
            bpy.context.object.modifiers["Solidify"].thickness += -0.5

        elif event.type == 'WHEELDOWNMOUSE':
            bpy.context.object.modifiers["Solidify"].thickness += 0.5

        elif event.type in {'LEFTMOUSE', "RIGHTMOUSE", "ESC"}:
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.object:
            obj = bpy.context.active_object
            obj = bpy.context.object

            if not obj.modifiers:
                bpy.ops.object.modifier_add(type='SOLIDIFY')
            for modifier in obj.modifiers:
                if modifier.type == 'SOLIDIFY':
                    pass
                elif modifier.type != 'SOLIDIFY':
                    obj.modifiers.clear()
                    bpy.ops.object.modifier_add(type='SOLIDIFY')

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}