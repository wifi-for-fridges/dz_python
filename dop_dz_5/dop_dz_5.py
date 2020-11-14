"""
Доп дз. Прочитать из excel файла любую таблицу и преобразовать её в формат json. Где ключами будут названия столбцов,
 а значениями - их содержимое
"""
from openpyxl import load_workbook
import json

wb = load_workbook('./dop_dz_5.xlsx')
sheet = wb.active

data = list(sheet.values)

surnames = []
for i in range(len(data[1])):
    for el in data[1:][i]:
        if el == data[1:][i][0]:
            surnames.append(el)

surnames = (data[0][0], surnames)

names = []
for i in range(len(data[1])):
    for el in data[1:][i]:
        if el == data[1:][i][1]:
            names.append(el)

names = (data[0][1], names)

sec_names = []
for i in range(len(data[1])):
    for el in data[1:][i]:
        if el == data[1:][i][2]:
            sec_names.append(el)

sec_names = (data[0][2], sec_names)

k_v_list = [surnames, names, sec_names]
new_form_d = {k: v for k, v in k_v_list}

with open('dop_zad_7.json', 'w') as f_json:
    json.dump(new_form_d, f_json)