import sys

import openpyxl as xl

from take_data import parse_raw_data

def enter_data_to_excel(data):
    cap_name = '№	f, MHz	P, dBm	IG, mA	ID, A	Gain, dB	КПД, %	Pвых, W'.split('\t')

    for i in data.keys():
        wb = xl.Workbook()

        print(i[:-4], data[i])

        meas = data[i]

        ws = wb.active
        wb.title = i[:-4]
        cap = False  # Наличие шапки(в первую строку)
        for block in range(1, 9):
            if not cap:
                ws.cell(1, block, cap_name[block - 1])

        for number, d in enumerate(meas['data']):
            ws.cell(int(number) + 2, 1, number)

            for x_instr in range(1, 8):
                ws.cell(int(number) + 2, x_instr + 1, d[x_instr - 1])

        ws.cell(1, 9, "max number")
        ws.cell(1, 10, number)
        wb.save(i[:-4] + '.xlsx')
        wb.close()


def main(args):
    if len(args) == 1:
        print('Error: data source path expected as an argument, abort.')
        return

    path = args[1]
    print(parse_raw_data(path))
    enter_data_to_excel(res)


if __name__ == '__main__':
    main(sys.argv)
