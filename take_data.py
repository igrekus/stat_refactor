import os
import re


def checkline(line):
    #  Шапка: (№); (f, MHz); (P, dBm); (IG, mA); (ID, A);	(Gain, dB); (КПД, %); (Pвых, W).
    work = line.replace(',', '.').split('\t')

    if not work[0].split('.')[0].isdecimal():
        return False

    index, *data = work
    index = int(float(index))

    freq = round(float(data[0]) / 1E+09, 2)
    power = round(float(data[1]), 3)
    values = [freq, power] + [float(v) for v in data[2:]]

    return [index, values]


def _filter_sources(path):
    filtered = []
    for file in os.listdir(path):
        joined = os.path.join(path, file)
        if os.path.isfile(joined) and joined.endswith('.txt'):
            filtered.append(joined)
    return filtered


def _filter_raw_data(lines):
    return [l.strip() for l in lines if l.startswith('№') or re.compile(r'^(\d+,\d+\s)+$').match(l)]


def _parse_file(file):
    data_list = {}
    with open(file, 'rt', encoding='utf-8') as f:
        raw_header, *raw_data = _filter_raw_data(f.readlines())
        for line in raw_data:
            x = checkline(line)
            if x:
                data_list[x[0]] = x[1]
    return data_list


def parse_raw_data(path):
    data_list_amp = {}
    for file in _filter_sources(path):
        data_list = _parse_file(file)
        data_list_amp[file] = data_list
    return data_list_amp


# x = take_data()
# for i in x.keys():
#     print(i[:-4], x[i])
