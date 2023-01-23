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


import argparse

parser = argparse.ArgumentParser()

parser.add_argument("mod_dir")

args = parser.parse_args()

print(args)