import bpy
import os
import inspect
from bpy.utils import register_class, unregister_class
from . import addon

# # run from same dir as Blender file instead of app addons dir
# # otherwise move to addon dir in (MacOS) /Applications/blender.app/Contents/X.xx/scripts/
# file = os.path.join(os.path.dirname(bpy.data.filepath), "addon.py")
# exec(compile(open(file)).read(), file, 'exec')

bl_info = {
    'name': 'Example Addon',
    'author': 'Botmasher (Joshua R)',
    'blender': (2, 79, 0),
    'version': (1, 0, 0),
    'location': 'View3D',
    'description': 'Demo of the structure of a Blender add-on',
    'category': 'Development'
}

def register_modules(modules, unregister=False):
    for module in modules:
        for member in inspect.getmembers(module, inspect.isclass):
            memberClass = member[1]
            try:
                registration = unregister_class(memberClass) if unregister else register_class(memberClass)
            except RuntimeError:
                print("Failed to load module member class {0}. Skipping for now.".format(memberClass))
    return

def register():
	register_modules([addon])

def unregister():
	register_modules(reverse([addon]), unregister=True)

__name__ == '__main__' and register()
