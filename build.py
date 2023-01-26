logo = """
____________       _ _     _ 
|  ___| ___ \     (_) |   | |
| |_  | |_/ /_   _ _| | __| |
|  _| | ___ \ | | | | |/ _` |
| |   | |_/ / |_| | | | (_| |
\_|   \____/ \__,_|_|_|\__,_|
"""

made_by = "Made by: Emanuele Ricci Lucchi aka EMALOK"

"""

program general function:

- From the directory th points to a factorio mod
- It works on the folder "mb" the is where the script is allowed to read and write
- In the folder mods/{mod_name}/mb/src is where to read the specification of the mod (gui etc)
- Given the specification the script the lua code in mods/{mod_name}/mb/build

sub works:

- gui
    - elaborate the gui given in the mods/{mod_name}/mb/src/gui/roots
    - fill in the components react style using the components in mods/{mod_name}/mb/src/gui/components
    - fill in styles using the files in mods/{mod_name}/mb/src/gui/styles

"""


# command line args helper
import argparse

# file access
import os

# cool and slick console logging
from console import *

# tasks
from tasks import gui


parser = argparse.ArgumentParser()

parser.add_argument("mod_dir",help="the root of the mod folder")

args = parser.parse_args()

# expand the arguments
mod_root_dir = args.mod_dir

print(logo)
print(made_by)

fbuild_root_dir = mod_root_dir + '/fbuild'
fbuild_src_root_dir = fbuild_root_dir + '/src'

# check that the folder fbuild exist
if not os.path.isdir(fbuild_root_dir):
    abort(f"fbuild folder not found in {os.path.abspath(mod_root_dir)}")

# check that the foldeer fbuild/src exist
if not os.path.isdir(fbuild_src_root_dir):
    abort(f"src folder not found in {os.path.abspath(fbuild_root_dir)}")

# this array contains function to call the different indipendent modules
#tasks: list[function]

tasks = [
    gui.gui_task
]

for current_task in tasks:

    current_task(fbuild_root_dir)