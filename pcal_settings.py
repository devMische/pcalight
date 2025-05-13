import bpy


class PCALsettings(bpy.types.PropertyGroup):

    # material/world checkboxes
    bpy.types.Scene.cb_matworld = bpy.props.BoolProperty(
        name="matworld", description="Apply material to the selected mesh", default=True)
