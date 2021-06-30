from argparse import Action, ArgumentParser
import os
import sys
import re


class VerifyIfFileExists(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        list_files = values
        for file_name in list_files:
            if os.path.isfile(file_name) and re.match(r'^.*\.j2$', file_name):
                namespace.jinjafile = file_name
            elif re.match(r'^.*(!\.j2)$', file_name):
                print(
                    "Invalid file extension\n"
                    + f"Used file name: {self.file_name}\n"
                    + "Expected file name to end with .j2"
                    + " example myjinjafile.txt.j2"
                )
                sys.exit(1)
            else:
                print("File doesn't exist")
                sys.exit(1)


class VerifyIfVariableIsValid(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        def VerifyVariable(variable):
            if re.match(r'^[a-zA-Z1-9-_]+=[^=]*$', variable):
                return variable.split("=")
            else:
                print(
                    "Value isn't on and acceptable format"
                    + " VARIABLE=VALUE,\n"
                    + " variables can make use of this character's"
                    + " a-z, A-Z, 1-9, - and _\n"
                    + f" you defined {variable}"
                )
                sys.exit(1)

        def BreakValueIfList(value):
            if re.match(r'^.*,.*$', value):
                return value.split(",")
            return value

        variables = values
        for variable in variables:
            try:
                name, value = VerifyVariable(variable)
                namespace.set[name] = BreakValueIfList(value)
            except Exception:
                namespace.set = {}
                name, value = VerifyVariable(variable)
                namespace.set[name] = BreakValueIfList(value)


class VerifyIfOutputPathIsValid(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        list_paths = values
        for file_path in list_paths:
            namespace.output = file_path


def CreateParser():
    parser = ArgumentParser(description='Render jinja files')
    parser.add_argument(
        "jinjafile",
        help="Pass jinja file",
        nargs=1,
        metavar=("JINJAFILE"),
        action=VerifyIfFileExists,
    )
    parser.add_argument(
        "--set",
        help="Declare variable to be used by the template",
        nargs=1,
        metavar=("PARAMETERS"),
        action=VerifyIfVariableIsValid,
        required=True,
    )
    parser.add_argument(
        "-v",
        help="Print the rendered file on the screen",
        action='store_true',
        default=False,
        required=False
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Choose where do you like the rendered file to be put",
        nargs=1,
        metavar=("OUTPUT"),
        action=VerifyIfOutputPathIsValid,
        required=False,
    )
    parser.add_argument(
        "--force",
        "-f",
        help="Force write and overwrite if file already exists",
        action='store_true',
        default=False,
        required=False,
    )
    return parser
