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
from . import addon_updater_ops

from . pcal_settings import PCALsettings
from . pcal_ui import PCAL_PT_main, PCAL_PT_camera
from . pcal_op_addpc import PCAL_OT_addpcop
from . pcal_op_addhs import PCAL_OT_addhsop
from . pcal_op_camviews import PCAL_OT_look360cam


bl_info = {
    "name": "PanoCamAdder Light",
    "author": "DerMische",
    "version": (1, 2, 1),
    "blender": (4, 3, 0),
    "location": "View3D > UI > PCA light",
    "description": "Free version of the PanoCamAdder",
    "warning": "",
    "doc_url": "https://der-mische.de/panocamadder/",
    "category": "3D View",
}


@addon_updater_ops.make_annotations
class PCALPreferences(bpy.types.AddonPreferences):
    """ preferences"""
    bl_idname = __package__

    # Addon updater preferences.

    auto_check_update = bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=False)

    updater_interval_months = bpy.props.IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0)

    updater_interval_days = bpy.props.IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
        max=31)

    updater_interval_hours = bpy.props.IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23)

    updater_interval_minutes = bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59)

    def draw(self, context):
        layout = self.layout

        # Works best if a column, or even just self.layout.
        mainrow = layout.row()
        col = mainrow.column()

        # Updater draw function, could also pass in col as third arg.
        addon_updater_ops.update_settings_ui(self, context)

        # Alternate draw function, which is more condensed and can be
        # placed within an existing draw function. Only contains:
        #   1) check for update/update now buttons
        #   2) toggle for auto-check (interval will be equal to what is set above)
        # addon_updater_ops.update_settings_ui_condensed(self, context, col)

        # Adding another column to help show the above condensed ui as one column
        # col = mainrow.column()
        # col.scale_y = 2
        # ops = col.operator("wm.url_open","Open webpage ")
        # ops.url=addon_updater_ops.updater.website


classes = (PCALsettings,
           PCAL_PT_main,
           PCAL_PT_camera,
           PCAL_OT_addpcop,
           PCAL_OT_addhsop,
           PCAL_OT_look360cam,
           PCALPreferences)


def register():
    addon_updater_ops.register(bl_info)
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    addon_updater_ops.unregister()
    for cls in classes:
        bpy.utils.unregister_class(cls)
