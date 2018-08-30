import bpy

bl_info = {
    'name': 'Example Addon',
    'author': 'Botmasher (Joshua R)',
    'blender': (2, 79, 0),
    'version': (1, 0, 0),
    'location': 'View3D',
    'description': 'Demo of the structure of a Blender add-on',
    'category': 'Development'
}

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
