from utils import *

def parse(k, v):
    return base_parse(k, v)

def clean(items):
    return items

data = parse_csv_data('./parking.csv', parse, clean, 1000)

print_dict(data[0])
