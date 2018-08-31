import bpy
import os

# run from same dir as Blender file instead of app addons dir
file = os.path.join(os.path.dirname(bpy.data.filepath), "addon.py")
exec(compile(open(file)).read(), file, 'exec')

bl_info = {
    'name': 'Example Addon',
    'author': 'Botmasher (Joshua R)',
    'blender': (2, 79, 0),
    'version': (1, 0, 0),
    'location': 'View3D',
    'description': 'Demo of the structure of a Blender add-on',
    'category': 'Development'
}
