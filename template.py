import os
from console import *

def build_template(template_name:str,template_data:list[tuple[str,str]]) -> str:
    # get template

    template_path = 'templates/' + template_name + '.template'

    if not os.path.isfile(template_path):
        abort(f"template '{template_name}' not found in templates")

    content = ""

    with open(template_path) as template:

        content = template.read()

        for curr_data in template_data:

            content = content.replace(curr_data[0],str(curr_data[1]))

    return content
