import bpy


class PCAL_PT_main(bpy.types.Panel):
    bl_label = "PCA light"
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
        col.operator("pcal.cam360", icon='CHECKBOX_HLT', text="OK")
