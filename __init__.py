# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Shapesafari",
    "description": "Create and Modify Meshs in Blender from Images",
    "author": "Lucas Dieckmann",
    "version": (1,0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf",
    "tracker_url": "https://github.com/lcsdmnn/Shapesafari/",
    "support": "COMMUNITY",
    "category": "User Interface"
}


import bpy


from .calibrate import SHAPESAFARI_OT_calibrate
from .image_to_mesh import SHAPESAFARI_OT_image_to_mesh
from .eraser import SHAPESAFARI_OT_eraser
from .extrude import SHAPESAFARI_OT_extrude
from .rotate import SHAPESAFARI_OT_rotatex, SHAPESAFARI_OT_rotatey, SHAPESAFARI_OT_rotatez
from .loft import SHAPESAFAFARI_OT_loft
from .bool import SHAPESAFARI_OT_bool_difference, SHAPESAFARI_OT_bool_union, SHAPESAFARI_OT_bool_intersect


def update_rotate(self, context):
    print(self.rotate_enum)
    eval('bpy.ops.%s()' % self.rotate_enum)


def update_bool(self, context):
    print(self.bool_enum)
    eval('bpy.ops.%s()' % self.bool_enum)






class SHAPESAFARI_PT_main_panel(bpy.types.Panel):
    '''This is the main panel of Shapesafari. All the Functionalities are displayed to the use here'''
    bl_idname = "shapesafari_PT_main_panel"
    bl_label = "SHAPESAFARI"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SHAPESAFARI"

    def draw(self, context):


        layout = self.layout


        box = layout.box()
        box.label(text="KALIBRIEREN", icon="MODIFIER")
        box.operator("shapesafari.calibrate_operator", text="Kalibrieren")

        box = layout.box()
        box.label(text="FOTO", icon="IMAGE_DATA")
        box.operator("shapesafari.imagetomesh_operator", text="Foto")

        box = layout.box()
        box.label(text="RADIERER", icon="SHADERFX")
        box.operator("shapesafari.eraser_operator", text="Radierer")

        box = layout.box()
        box.label(text="EXTRUDIEREN", icon="MESH_CUBE")
        box.operator("shapesafari.extrude_operator", text="Extrudieren")

        row = layout.row()
        box = layout.box()
        box.label(text="ROTIEREN", icon="MESH_CYLINDER")
        box.prop(context.scene, 'rotate_enum', expand=True)



        box = layout.box()
        box.label(text="LOFTEN", icon="MESH_CONE")
        box.operator("shapesafari.loft_operator", text="Loften")

        box = layout.box()
        box.label(text="BOOL", icon="MOD_BOOLEAN")
        box.prop(context.scene, 'bool_enum', expand=True)

        row = layout.row()

        box = layout.box()
        box.label(text="Save", icon="FILEBROWSER")


def register():
    bpy.utils.register_class(SHAPESAFARI_PT_main_panel)
    bpy.utils.register_class(SHAPESAFARI_OT_calibrate)
    bpy.utils.register_class(SHAPESAFARI_OT_image_to_mesh)
    bpy.utils.register_class(SHAPESAFARI_OT_eraser)
    bpy.utils.register_class(SHAPESAFARI_OT_extrude)
    bpy.utils.register_class(SHAPESAFARI_OT_rotatex)
    bpy.utils.register_class(SHAPESAFARI_OT_rotatey)
    bpy.utils.register_class(SHAPESAFARI_OT_rotatez)
    bpy.utils.register_class(SHAPESAFAFARI_OT_loft)
    bpy.utils.register_class(SHAPESAFARI_OT_bool_difference)
    bpy.utils.register_class(SHAPESAFARI_OT_bool_union)
    bpy.utils.register_class(SHAPESAFARI_OT_bool_intersect)

    bpy.types.Scene.rotate_enum = bpy.props.EnumProperty(name = "Rotate Enum", description = "Rotate Enum",
            items = [
                ("shapesafari.rotatex_operator", "X-Axis", "Rotate the object around the X-Axis"),
                ("shapesafari.rotatey_operator", "Y-Axis", "Rotate the object around the Y-Axis"),
                ("shapesafari.rotatez_operator", "Z-Axis", "Rotate the object around the Z-Axis")
            ],
            update=update_rotate
        )

    bpy.types.Scene.bool_enum = bpy.props.EnumProperty(name = "Bool enum", description = "My enum description",
            items = [

                ("shapesafari.booldifference_operator", "Abziehen", "Subtract the two solids from each other"),
                ("shapesafari.boolunion_operator", "Verbinden", "Join the two volumes"),
                ("shapesafari.boolintersect_operator", "Uerbschneiden", "Get the intersection of the two volumes")
            ],
            update=update_bool
        )




def unregister():
    bpy.utils.unregister_class(SHAPESAFARI_PT_main_panel)
    bpy.utils.unregister_class(SHAPESAFARI_OT_calibrate)
    bpy.utils.unregister_class(SHAPESAFARI_OT_image_to_mesh)
    bpy.utils.unregister_class(SHAPESAFARI_OT_eraser)
    bpy.utils.unregister_class(SHAPESAFARI_OT_extrude)
    bpy.utils.unregister_class(SHAPESAFARI_OT_rotatex)
    bpy.utils.unregister_class(SHAPESAFARI_OT_rotatey)
    bpy.utils.unregister_class(SHAPESAFARI_OT_rotatez)
    bpy.utils.unregister_class(SHAPESAFAFARI_OT_loft)
    bpy.utils.unregister_class(SHAPESAFARI_OT_bool_difference)
    bpy.utils.unregister_class(SHAPESAFARI_OT_bool_union)
    bpy.utils.unregister_class(SHAPESAFARI_OT_bool_intersect)



if __name__ == "__main__":
    register()