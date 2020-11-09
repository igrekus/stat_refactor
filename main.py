import sys

from take_data import take_data_txt


def main(args):
    if len(args) == 1:
        print('Error: data source path expected as an argument, abort.')
        return
    path = args[1]
    print(path)

    print(take_data_txt())


if __name__ == '__main__':
    main(sys.argv)
