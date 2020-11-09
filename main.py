import sys


def main(args):
    if len(args) == 1:
        print('Error: data source path expected as an argument, abort.')
        return
    path = args[1]
    print(path)


if __name__ == '__main__':
    main(sys.argv)
