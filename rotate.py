import bpy

def set_origin():
    area_type = 'VIEW_3D'
    areas  = [area for area in bpy.context.window.screen.areas if area.type == area_type]
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')

    bpy.context.scene.tool_settings.use_transform_data_origin = True

    with bpy.context.temp_override(area=areas[0]):
        bpy.ops.transform.create_orientation(use=True)
        bpy.ops.object.editmode_toggle()
        transform_type = bpy.context.scene.transform_orientation_slots[0].type
        bpy.ops.transform.transform(mode='ALIGN', orient_type='Face', orient_matrix_type=transform_type, mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='ACTIVE', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
        bpy.ops.transform.delete_orientation()
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')
    bpy.context.scene.tool_settings.use_transform_data_origin = False


class SHAPESAFARI_OT_rotatex(bpy.types.Operator):
    """Rotate an Object along an axis"""
    bl_idname = "shapesafari.rotatex_operator"
    bl_label = "Rotate X Axis"


    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        if context.object:
            obj = bpy.context.active_object
            obj = bpy.context.object
            set_origin()

            if not obj.modifiers:
                bpy.ops.object.modifier_add(type='SCREW')
                bpy.context.object.modifiers["Screw"].axis = "X"
                bpy.ops.object.modifier_apply()


            for modifier in obj.modifiers:
                if modifier.type == "SCREW":

                    bpy.ops.object.modifier_remove(modifier="Screw", report=False)
                    bpy.ops.object.modifier_add(type='SCREW')
                    bpy.context.object.modifiers["Screw"].axis = "X"
                    bpy.ops.object.modifier_apply()

                elif modifier.type != "SCREW":

                    bpy.ops.object.modifier_add(type='SCREW')
                    bpy.context.object.modifiers["Screw"].axis = "X"
                    bpy.ops.object.modifier_apply()
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

        return {'FINISHED'}




class SHAPESAFARI_OT_rotatey(bpy.types.Operator):
    """Rotate an Object along an axis"""
    bl_idname = "shapesafari.rotatey_operator"
    bl_label = "Rotate Y Axis"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        if context.object:
            obj = bpy.context.active_object
            obj = bpy.context.object
            set_origin()

            if not obj.modifiers:
                bpy.ops.object.modifier_add(type='SCREW')
                bpy.context.object.modifiers["Screw"].axis = "Y"
                bpy.ops.object.modifier_apply()

            for modifier in obj.modifiers:
                if modifier.type == "SCREW":

                    bpy.ops.object.modifier_remove(modifier="Screw", report=False)
                    bpy.ops.object.modifier_add(type='SCREW')
                    bpy.context.object.modifiers["Screw"].axis = "Y"
                    bpy.ops.object.modifier_apply()

                elif modifier.type != "SCREW":

                    bpy.ops.object.modifier_add(type='SCREW')
                    bpy.context.object.modifiers["Screw"].axis = "Y"
                    bpy.ops.object.modifier_apply()
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

        return {'FINISHED'}


class SHAPESAFARI_OT_rotatez(bpy.types.Operator):
    """Rotate an Object along an axis"""
    bl_idname = "shapesafari.rotatez_operator"
    bl_label = "Rotate Z Axis"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        if context.object:
            obj = bpy.context.active_object
            obj = bpy.context.object
            set_origin()

            if not obj.modifiers:
                bpy.ops.object.modifier_add(type='SCREW')
                bpy.context.object.modifiers["Screw"].axis = "Z"
                bpy.ops.object.modifier_apply()

            for modifier in obj.modifiers:
                if modifier.type == "SCREW":

                    bpy.ops.object.modifier_remove(modifier="Screw", report=False)
                    bpy.ops.object.modifier_add(type='SCREW')
                    bpy.context.object.modifiers["Screw"].axis = "Z"
                    bpy.ops.object.modifier_apply()

                elif modifier.type != "SCREW":

                    bpy.ops.object.modifier_add(type='SCREW')
                    bpy.context.object.modifiers["Screw"].axis = "Z"
                    bpy.ops.object.modifier_apply()
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

        return {'FINISHED'}
