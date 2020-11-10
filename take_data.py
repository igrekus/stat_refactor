import os
import re


def _parse_line(line):
    # return normalized data raw
    # freq in GHz; pow rounded to 3rd place; the rest of the data as is
    data = line.replace(',', '.').split('\t')[1:]
    return [round(float(data[0]) / 1E+09, 2), round(float(data[1]), 3)] + [float(v) for v in data[2:]]


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
    return {'header': [str(el) for el in raw_header.split('\t')[1:]], 'data': [_parse_line(line) for line in raw_data]}


def parse_raw_data(path):
    data_list_amp = {}
    for file in _filter_sources(path):
        data_list_amp[file] = _parse_file(file)
    return data_list_amp


# x = take_data()
# for i in x.keys():
#     print(i[:-4], x[i])
