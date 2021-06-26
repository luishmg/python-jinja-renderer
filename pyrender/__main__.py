from .render import JinjaRender
from .cli import CreateParser
import sys
import re


def main(argv=None):
    args = CreateParser().parse_args(argv)
    jinjaFile = JinjaRender(args.jinjafile, args.set, args.output)
    if args.v:
        print(jinjaFile.RenderTemplate())
    message = jinjaFile.RenderJinjaFile()
    print(message)
    if re.match(r'^.*Fail.*$', message):
        return 1
    return 0


def init(argv=None):
    if __name__ == '__main__':
        sys.exit(int(main(argv)))


init()
