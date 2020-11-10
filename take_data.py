import os
import re


def checkline(line):
    #  Шапка: (№); (f, MHz); (P, dBm); (IG, mA); (ID, A);	(Gain, dB); (КПД, %); (Pвых, W).
    data = line.replace(',', '.').split('\t')[1:]

    freq = round(float(data[0]) / 1E+09, 2)
    power = round(float(data[1]), 3)

    return [freq, power] + [float(v) for v in data[2:]]


def _filter_sources(path):
    filtered = []
    for file in os.listdir(path):
        joined = os.path.join(path, file)
        if os.path.isfile(joined) and joined.endswith('.txt'):
            filtered.append(joined)
    return filtered


def _filter_raw_data(lines):
    return [l.strip() for l in lines if l.startswith('№') or re.compile(r'^(-?\d+,\d+\s)+$').match(l)]


def _parse_file(file):
    with open(file, 'rt', encoding='utf-8') as f:
        raw_header, *raw_data = _filter_raw_data(f.readlines())
    return [str(el) for el in raw_header.split('\t')], {idx + 1: checkline(line) for idx, line in enumerate(raw_data)}


def parse_raw_data(path):
    data_list_amp = {}
    for file in _filter_sources(path):
        header, data_list = _parse_file(file)
        data_list_amp[file] = data_list
    return data_list_amp


# x = take_data()
# for i in x.keys():
#     print(i[:-4], x[i])
