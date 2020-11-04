import os


def checkline(line):
    #  Шапка: (№); (f, MHz); (P, dBm); (IG, mA); (ID, A);	(Gain, dB); (КПД, %); (Pвых, W).
    line = line.replace(',', '.')
    work = line.split('	')

    if work[0].split('.')[0]. isdecimal( ):
        number = int(work[0].split('.')[0])
        data_line = [round(int(work[1].split('.')[0])/1E+09 , 2),
                     round(float(work[2]), 3),
                     float(work[3]),
                     float(work[4]),
                     float(work[5]),
                     float(work[6]),
                     float(work[7])]
        # print([number, data_line])
        return [number, data_line]
    return False


def take_data_txt():
    if  'dates' not in os.getcwd():
        os.chdir('dates')
        Datas = os.listdir()

    else:
        Datas = os.listdir()



    data_list_amp = {}
    for i in Datas:
        data_list = {}
        with open(i, 'r') as f:
            for line in f:
                line = line.strip()
                # print(line)
                x = checkline(line)
                if x:
                    data_list[x[0]] = x[1]
        data_list_amp[i] = data_list

    return data_list_amp



# x = take_data()
# for i in x.keys():
#     print(i[:-4], x[i])