# Example Blender Python Addon

Demonstrating the structure of a Blender Python Add-on.

## Installation

The only dependency is a working version of [Blender](https://www.blender.org/download/) (developed on 2.79), though Python, your preferred IDE and command line tools will be useful for development.
 Here are steps for installing Example Addon inside Blender:
- Place the contents of this addon inside your local Blender's `scripts/addons_contrib`
- Run Blender
- Open `User Preferences`
- Select `Add-ons` and limit the supported level to `Testing`
- Find and enable Example Addon

Once Example Addon is enabled, you will see a new panel in the tool bar alongside the 3D View. Press the button to send a message to your console (visible when running Blender from terminal).

## Development

You can use this project as a template for developing your own Blender add-on. Follow the installation instructions above, then play with the UI in `addon.py`, add your own functionality, and change the imports in `__init__.py` as you like.

Note that the initialization file reads through all classes in `addon.py`, so react to or change this loop to if you need to avoid or alter its reach.

## Notes & Research

These are a few scrambled notes I took while developing Example Addon. I'll leave them here for reference and maybe future cleanup.

- understanding file storage / search on Mac OS
  - app in `/Applications/`, user data in `~/Library/`
  - off app dir: `/Applications/Blender.app/Contents/Resources/2.xx/scripts/addons`
  - off user dir: `~/Library/Application Support/Blender/2.xx/`
  - I don't see the app dir
    - ok it's here for me: `/Applications/blender.app` (lowercase `b`)
    - inside `scripts/` there I found my old test `slide-into-view`; will look into and take notes on this
  - reportedly Blender [checks three locations](https://blender.stackexchange.com/questions/23517/need-help-installing-addon-on-mac)
- imported from addon.py
- added register/unregister for all classes in imported module
- in User Preferences > Add-ons make sure Testing is selected
