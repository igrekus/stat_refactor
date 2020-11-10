import os
import sys

import openpyxl as xl

from take_data import parse_raw_data


def export_to_excel(parsed_data, export_folder='excel'):
    for file_name, file_data in parsed_data.items():
        out_file = file_name.split('\\')[-1][:-4]

        wb = xl.Workbook()
        ws = wb.active
        wb.title = out_file

        ws.append(['№'] + file_data['header'] + ['max number'] + [len(file_data['data'])])

        for number, d in enumerate(file_data['data']):
            ws.append([number] + d)

        wb.save(f'{os.path.join(export_folder, out_file)}.xlsx')
        wb.close()


def main(args):
    if len(args) == 1:
        print('Error: data source path expected as an argument, abort.')
        return

    path = args[1]

    res = parse_raw_data(path)

    export_to_excel(res)


if __name__ == '__main__':
    main(sys.argv)
