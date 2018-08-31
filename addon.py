import bpy

class ExampleAddon (bpy.types.Operator):
    bl_idname = 'object.example_addon'
    bl_label = 'Object example addon'

    def execute (self, ctx):
        print("Running Example Addon!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ExampleAddon)

def unregister():
    bpy.utils.unregister_class(ExampleAddon)

name == '__main__' and register()
