import bpy

class ExampleAddonPanel (bpy.types.Panel):
    bl_idname = 'object.example_addon_panel'
    bl_label ='Example Addon'
    bl_category = 'Addon Test UI'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw (self, ctx):
        layout = self.layout
        layout.operator('object.example_addon', text="Display Console Text")

class ExampleAddon (bpy.types.Operator):
    bl_idname = 'object.example_addon'
    bl_label = 'Run Example Addon'

    def execute (self, ctx):
        print("Running Example Addon!")
        return {'FINISHED'}
