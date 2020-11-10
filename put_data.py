import os
import openpyxl


def export_to_excel(parsed_data, export_folder='excel'):
    for file_name, file_data in parsed_data.items():
        out_file = file_name.split('\\')[-1][:-4]

        wb = openpyxl.Workbook()
        ws = wb.active
        wb.title = out_file

        ws.append(['№'] + file_data['header'] + ['max number'] + [len(file_data['data'])])

        for number, d in enumerate(file_data['data']):
            ws.append([number] + d)

        wb.save(f'{os.path.join(export_folder, out_file)}.xlsx')
        wb.close()
