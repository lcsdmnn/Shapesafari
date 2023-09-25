import bpy


class SHAPESAFARI_OT_bool_difference(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "shapesafari.booldifference_operator"
    bl_label = "Bool Tool"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        if context.object:
            obj = bpy.context.active_object
            selected_objs = [obj for obj in bpy.context.selected_objects if obj != bpy.context.active_object]


            if not obj.modifiers:
                bpy.ops.object.modifier_add(type='BOOLEAN')
                bpy.context.object.modifiers["Boolean"].operation = "DIFFERENCE"
                bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                bpy.ops.object.modifier_apply()
                bpy.data.objects[selected_objs[0].name].hide_viewport = True

            for modifier in obj.modifiers:
                if modifier.type == "BOOLEAN":

                    bpy.ops.object.modifier_remove(modifier="BOOLEAN", report=False)
                    bpy.context.object.modifiers["Boolean"].operation = "DIFFERENCE"
                    bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                    bpy.ops.object.modifier_apply()
                    bpy.data.objects[selected_objs[0].name].hide_viewport = True


                elif modifier.type != "BOOLEAN":
                    bpy.ops.object.modifier_add(type='BOOLEAN')
                    bpy.context.object.modifiers["Boolean"].operation = "DIFFERENCE"
                    bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                    bpy.ops.object.modifier_apply()

                    bpy.data.objects[selected_objs[0].name].hide_viewport = True



        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

        return {'FINISHED'}


class SHAPESAFARI_OT_bool_union(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "shapesafari.boolunion_operator"
    bl_label = "Simple Modal Operator"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        if context.object:
            obj = bpy.context.active_object
            selected_objs = [obj for obj in bpy.context.selected_objects if obj != bpy.context.active_object]

            print(selected_objs)

            if not obj.modifiers:
                bpy.ops.object.modifier_add(type='BOOLEAN')
                bpy.context.object.modifiers["Boolean"].operation = "UNION"

                bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                bpy.ops.object.modifier_apply()
                bpy.data.objects[selected_objs[0].name].hide_viewport = True

            for modifier in obj.modifiers:
                if modifier.type == "BOOLEAN":

                    bpy.ops.object.modifier_remove(modifier="BOOLEAN", report=False)
                    bpy.context.object.modifiers["Boolean"].operation = "UNION"

                    bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                    bpy.ops.object.modifier_apply()
                    bpy.data.objects[selected_objs[0].name].hide_viewport = True


                elif modifier.type != "BOOLEAN":
                    bpy.ops.object.modifier_add(type='BOOLEAN')
                    bpy.context.object.modifiers["Boolean"].operation = "UNION"

                    bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                    bpy.ops.object.modifier_apply()

                    bpy.data.objects[selected_objs[0].name].hide_viewport = True



        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

        return {'FINISHED'}


class SHAPESAFARI_OT_bool_intersect(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "shapesafari.boolintersect_operator"
    bl_label = "Simple Modal Operator"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        if context.object:
            obj = bpy.context.active_object
            selected_objs = [obj for obj in bpy.context.selected_objects if obj != bpy.context.active_object]
            print(selected_objs)

            if not obj.modifiers:
                bpy.ops.object.modifier_add(type='BOOLEAN')
                bpy.context.object.modifiers["Boolean"].operation = "INTERSECT"

                bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                bpy.ops.object.modifier_apply()
                bpy.data.objects[selected_objs[0].name].hide_viewport = True

            for modifier in obj.modifiers:
                if modifier.type == "BOOLEAN":

                    bpy.ops.object.modifier_remove(modifier="BOOLEAN", report=False)
                    bpy.context.object.modifiers["Boolean"].operation = "INTERSECT"

                    bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                    bpy.ops.object.modifier_apply()
                    bpy.data.objects[selected_objs[0].name].hide_viewport = True


                elif modifier.type != "BOOLEAN":
                    bpy.ops.object.modifier_add(type='BOOLEAN')
                    bpy.context.object.modifiers["Boolean"].operation = "INTERSECT"

                    bpy.context.object.modifiers["Boolean"].object = selected_objs[0]
                    bpy.ops.object.modifier_apply()

                    bpy.data.objects[selected_objs[0].name].hide_viewport = True



        else:
            self.report({'WARNING'}, "No active object, could not finish")
            return {'CANCELLED'}

        return {'FINISHED'}