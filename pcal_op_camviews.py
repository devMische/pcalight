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
from . pcal_funcs import replace_last


class PCAL_OT_look360cam(bpy.types.Operator):
    """ Select and activate camera"""
    bl_idname = "pcal.cam360"
    bl_label = "Set 360° View"

    def execute(self, context):

        if bpy.context.scene.camera is None:
            self.report({'WARNING'}, "No camera found ..")
            return {'CANCELLED'}
        else:
            bpy.context.space_data.camera = bpy.context.scene.camera
            bpy.context.space_data.use_local_camera = True
            bpy.context.space_data.lock_camera = True

            cb_matworld = context.scene.cb_matworld

            if cb_matworld == True:
                if context.mode == 'OBJECT':
                    er = False
                    ertext = ''

                    # world
                    wo = bpy.context.scene.camera.name
                    worldname = replace_last(wo, "_CAM", "_WORLD")
                    if worldname in bpy.data.worlds:
                        bpy.context.scene.world = bpy.data.worlds[worldname]
                    else:
                        er = True
                        ertext += 'no world found .. '

                    # material
                    obj = bpy.context.active_object
                    if obj.type == 'MESH':

                        obj.select_set(True)  # Select the object
                        context.view_layer.objects.active = obj  # Set the object as the active object

                        ma = bpy.context.scene.camera.name
                        matname = replace_last(ma, "_CAM", "_MAT")

                        if matname in bpy.data.materials:
                            for i in range(len(obj.material_slots)):
                                obj.active_material_index = 0
                                bpy.ops.object.material_slot_remove()

                            obj.active_material = bpy.data.materials[matname]
                        else:
                            er = True
                            ertext += 'no material found .. '

                    else:
                        er = True
                        ertext += 'no MESH selected .. '

                    if er == True:
                        self.report({'WARNING'}, ertext)
                else:
                    self.report(
                        {'WARNING'}, "Can't apply material. Switch to object-mode!")

            return {'FINISHED'}
