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

from . pcal_settings import PCALsettings
from . pcal_ui import PCAL_PT_main, PCAL_PT_camera
from . pcal_op_addpc import PCAL_OT_addpcop
from . pcal_op_addhs import PCAL_OT_addhsop
from . pcal_op_camviews import PCAL_OT_look360cam


bl_info = {
    "name": "PanoCamAdder-Light",
    "author": "DerMische",
    "version": (1, 0, 0),
    "blender": (4, 3, 0),
    "location": "View3D > UI > PCA light",
    "description": "Free version of the PanoCamAdder",
    "warning": "",
    "doc_url": "https://der-mische.de/panocamadder/",
    "category": "3D View",
}


classes = (PCALsettings,
           PCAL_PT_main,
           PCAL_PT_camera,
           PCAL_OT_addpcop,
           PCAL_OT_addhsop,
           PCAL_OT_look360cam)


register, unregister = bpy.utils.register_classes_factory(classes)
