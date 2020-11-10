import openpyxl as xl
import os


def take_data_excel():
    if 'excel' not in os.getcwd():
        os.chdir('excel')

    Datas = os.listdir()

    if 'unity.xlsx' in Datas:
        wb_unity = xl.load_workbook('unity.xlsx')  # Файл соединенный из других файлов
    else:
        wb_unity = xl.Workbook()
        return False

    if len(Datas) == 0:
        print('No unity.xlsx file')
        return False
