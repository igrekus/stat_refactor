import sys

from take_data import parse_raw_data
from put_data import export_to_excel


def main(args):
    if len(args) == 1:
        print('Error: data source path expected as an argument, abort.')
        return

    path = args[1]
    res = parse_raw_data(path)
    export_to_excel(res)


if __name__ == '__main__':
    main(sys.argv)
