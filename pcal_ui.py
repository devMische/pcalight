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


import bpy


class PCAL_PT_main(bpy.types.Panel):
    bl_label = "PCA light 1.2.1"
    bl_idname = "PCAL_PT_Main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "PCA light"

    def draw(self, context):
        if context.mode == 'OBJECT':

            layout = self.layout
            col = layout.column(align=True)
            col.operator("pcal.addpcop", text="Add PanoCam",
                         icon='CON_CAMERASOLVER')
            col.operator("pcal.addhsop", icon='MOD_MASK')
            layout.scale_y = 1.3

        else:

            layout = self.layout
            box = layout.box()
            box.label(text=" Switch to object-mode")


class PCAL_PT_camera(bpy.types.Panel):
    """Camera Settings"""
    bl_label = "PanoCam Viewer"
    bl_idname = "PCAL_PT_camera"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "PCA light"
    bl_parent_id = 'PCAL_PT_Main'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        scene = context.scene

        layout = self.layout
        col = layout.column()
        col.prop(scene, "camera", text="")
        col.prop(scene, "cb_matworld", text='Assign PanoMAT')
        col.operator("pcal.cam360", icon='CHECKBOX_HLT', text="OK")
