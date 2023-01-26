
import os
import glob
from console import *
from template import build_template
import re


"""
converts a css decl to a factorio lua style line

ex:

margin: 10

V

[
    ("top_margin", 10),
    ("right_margin", 10),
    ("bottom_margin", 10),
    ("left_margin", 10)
]

"""

def stringify(string) -> str:
    return f'"{string}"'

def css_generate_style_name(css_selector) -> str:
    return "LuaStyle_name"


def css_convert_decl(property, args) -> list:

    # IMPORTANT use stringify when returning something that needs quotes

    args_count = len(args)

    if property == "padding":
        # can accept 1, 2 or 4 args

        if args_count == 1:

            # top/bottom/right/left are set to the args

            ret = []
            try:
                ret.append(("padding_top", int(args[0])))
                ret.append(("padding_right", int(args[0])))
                ret.append(("padding_bottom", int(args[0])))
                ret.append(("padding_left", int(args[0])))
            except ValueError:
                error(
                    f"[GUI] [CSS] padding1 arguments couldn't be conveted to int args: {args}")
                return []

            return ret

        elif args_count == 2:

            # top/bottom right/left are set to the args

            ret = []
            try:
                ret.append(("padding_top", int(args[0])))
                ret.append(("padding_right", int(args[1])))
                ret.append(("padding_bottom", int(args[0])))
                ret.append(("padding_left", int(args[1])))
            except ValueError:
                error(
                    f"[GUI] [CSS] padding2 arguments couldn't be conveted to int args: {args}")
                return []

            return ret

        elif args_count == 4:

            # top right bottom left are set to the args

            ret = []
            try:
                ret.append(("padding_top", int(args[0])))
                ret.append(("padding_right", int(args[1])))
                ret.append(("padding_bottom", int(args[2])))
                ret.append(("padding_left", int(args[3])))
            except ValueError:
                error(
                    f"[GUI] [CSS] padding4 arguments couldn't be conveted to int args: {args}")
                return []

            return ret

        else:
            error(
                f"[GUI] [CSS] padding expects 1, 2 or 4 arguments but {args_count} were given")
            return []

    elif property == "margin":
        pass

    warning(f"[GUI] [CSS] no matching property for {property}")
    return []


def css_compress_expressions(expressions_list):

    return_list = []

    for i in range(len(expressions_list)):

        # check if it is alredy in the return list

        present = False  # if the expression is in the return list
        present_index = -1  # where the expression is the retur list

        for j in range(len(return_list)):

            if expressions_list[i][0] == return_list[j][0]:
                present = True
                present_index = j

        if present:
            # modify the expresion with the new value
            return_list[present_index] = expressions_list[i]
        else:
            # append the expression to the return list
            return_list.append(expressions_list[i])

    return return_list


def gui_task(fbuild_dir):
    log("[GUI] start")

    src_dir = fbuild_dir + '/src'
    gui_dir = src_dir + '/gui'

    # require a gui fulder inside the src folder
    if not os.path.isdir(gui_dir):
        abort(f"gui folder not found in {os.path.abspath(src_dir)}")

    # all files that end in xml
    xml_gen_targets = glob.glob(gui_dir + "/*.xml")

    # check if components folder exist
    components_dir = gui_dir + '/components'

    if not os.path.isdir(components_dir):
        warning(f"components folder not found in {os.path.abspath(gui_dir)}")

    xml_comp_gen_targets = glob.glob(components_dir + '/*.xml')

    # check if styles folder exist
    styles_dir = gui_dir + '/styles'

    if not os.path.isdir(styles_dir):
        warning(f"styles folder not found in {os.path.abspath(gui_dir)}")

    css_gen_targets = glob.glob(styles_dir + '/*.css')

    log(f"[GUI] gui roots count: {len(xml_gen_targets)}")
    log(f"[GUI] gui component count: {len(xml_comp_gen_targets)}")
    log(f"[GUI] gui style count: {len(css_gen_targets)}")

    # print(xml_gen_targets)
    # print(xml_comp_gen_targets)
    # print(css_gen_targets)

    # CSS BUILDING
    css_comment_regex = re.compile(r"\/\*[\s\S]*?\*\/")
    css_statement_regex = re.compile(r'([.#]?\w+)\s*{([\s\S]*?)}')


    for curr_style_file in css_gen_targets:

        # read file
        content = ""
        with open(curr_style_file) as file:
            content = file.read()

        # remove comments
        uncommented_content = css_comment_regex.sub("", content)

        style_blocks = []

        # match css expressions
        for curr_match in css_statement_regex.finditer(uncommented_content):

            (selector, body) = curr_match.groups()

            statements = body.split(';')
            for i in range(len(statements)):
                statements[i] = statements[i].strip()

                # remove empty elements
                while '' in statements:
                    statements.remove('')

            expressions = []

            for curr_statement in statements:

                (key_word, args) = curr_statement.split(':', 1)

                key_word = key_word.strip()
                args = args.strip()

                args_list = args.split(" ")

                while '' in args_list:
                    args_list.remove('')

                ret = css_convert_decl(key_word, args_list)

                if len(ret) > 0:
                    expressions.extend(ret)

            # print("from",expressions)

            compressed_css_expressions = css_compress_expressions(expressions)

            # print("to",compressed_css_expressions)

            style_exprs = []

            for curr_expr in compressed_css_expressions:

                style_exprs.append(
                    build_template(
                        'style-expr',
                        [
                            ('--PROPERTY-NAME--', curr_expr[0]),
                            ('--PROPERTY-VALUE--',curr_expr[1])
                        ]
                    )
                )

            style_body = ""
                
            for i in range(len(style_exprs)):

                style_body += '\t' + style_exprs[i]

                if i != len(style_exprs) - 1:
                    style_body += ',\n'

            style_name = stringify(css_generate_style_name(selector))

            style_blocks.append(
                build_template(
                    'style-decl-block',
                    [
                        ('--STYLE-NAME--',style_name),
                        ('--STYLE-BODY--',style_body)
                    ]
                )
            )
        
        file_body = ""
                
        for i in range(len(style_blocks)):

            file_body += style_blocks[i]

            if i != len(style_blocks) - 1:
                file_body += '\n\n\n'

        #print(file_body)

        file_content = build_template(
            'lua-header',
            [
                ('--BODY--',
                    build_template(
                        'style-header',
                        [
                            ('--BODY--',file_body)
                        ]
                    )
                )
            ]
        )
        
        file_path = f'{fbuild_dir}/build/gui/{str(os.path.basename(curr_style_file)).split(".",1)[0]}.lua'

        # generate the parent folder
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path,'w') as file:
            file.write(file_content)
