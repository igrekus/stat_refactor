import sys

from take_data import parse_raw_data


def main(args):
    if len(args) == 1:
        print('Error: data source path expected as an argument, abort.')
        return

    path = args[1]
    print(parse_raw_data(path))


if __name__ == '__main__':
    main(sys.argv)
