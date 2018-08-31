# Example Blender Python Addon

Checking and demonstrating the structure of a basic Blender Python addon. This project is stored in .

## Installation

Place the contents of this addon inside your local Blender folder's `scripts/addons`.

## Notes & Research
- understanding file storage / search on Mac OS
  - app in `/Applications/`, user data in `~/Library/`
  - off app dir: `/Applications/Blender.app/Contents/Resources/2.xx/scripts/addons`
  - off user dir: `~/Library/Application Support/Blender/2.xx/`
  - I don't see the app dir
    - ok it's here for me: `/Applications/blender.app` (lowercase `b`)
    - inside `scripts/` there I found my old test `slide-into-view`; will look into and take notes on this
  - reportedly Blender [checks three locations](https://blender.stackexchange.com/questions/23517/need-help-installing-addon-on-mac)
