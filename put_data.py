import os
import openpyxl


def export_to_excel(parsed_data, export_folder='excel'):
    wb_compiled = openpyxl.Workbook()
    ws_plots = wb_compiled.active

    for file_name, file_data in parsed_data.items():
        out_file = file_name.split('\\')[-1][:-4]

        wb = openpyxl.Workbook()
        ws = wb.active
        wb.title = out_file

        ws_compiled = wb_compiled.create_sheet(out_file)

        header = ['№'] + file_data['header'] + ['max number'] + [len(file_data['data'])]
        ws.append(header)
        ws_compiled.append(header)

        for number, d in enumerate(file_data['data']):
            row = [number] + d
            ws.append(row)
            ws_compiled.append(row)

        wb.save(f'{os.path.join(export_folder, out_file)}.xlsx')
        wb.close()

        wb_compiled.save(f'{os.path.join(export_folder, "compiled")}.xlsx')
        wb_compiled.close()
