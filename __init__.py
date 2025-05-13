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
    "wiki_url": "https://der-mische.de/panocamadder/",
    "category": "3D View",
}


classes = (PCALsettings,
           PCAL_PT_main,
           PCAL_PT_camera,
           PCAL_OT_addpcop,
           PCAL_OT_addhsop,
           PCAL_OT_look360cam)


register, unregister = bpy.utils.register_classes_factory(classes)
