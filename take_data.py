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


def _filter_sources(path):
    filtered = []
    for file in os.listdir(path):
        joined = os.path.join(path, file)
        if os.path.isfile(joined) and joined.endswith('.txt'):
            filtered.append(joined)
    return filtered


def parse_raw_data(path):
    data_list_amp = {}
    for file in _filter_sources(path):
        data_list = {}
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                # print(line)
                x = checkline(line)
                if x:
                    data_list[x[0]] = x[1]
        data_list_amp[file] = data_list

    return data_list_amp


# x = take_data()
# for i in x.keys():
#     print(i[:-4], x[i])
