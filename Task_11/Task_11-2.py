#! /usr/bin/python

# Задача 11-2
#  - Дан файл с расширением .csv ,
#  содержащий в каждой строчке следующую информацию:
#  номер, фамилия, имя, компания, зарплата.
#  - Создайте Эксельный файл, в который перенесите эту информацию,
#  предварительно отсортировав этот список по компании, по фамилии и имени.
#  - В конце списка добавьте строку: ИТОГО и суммарное значение всех зарплат.

# Импортируем модуль openpyxl
import csv

import openpyxl

row = {}
dct = {}
srt = ""
wb = openpyxl.Workbook()
with open('Task_11-2.csv') as f:
    reader = csv.reader(f, delimiter=' ', quotechar='|')
    # reader = csv.DictReader(f)
    for row in reader:
        print(', '.join(row).split(','))

# with open("Task_11-2.csv", "r") as f:
#     # итерация по строкам
#     for line in f:
#         l = line.strip('\n').split(',')
#         dct
#         print(type(l))
#         for i in l:
#             print(type(i))
#             print(i)
#         input()

# z = []
# with open('Task_11-2.csv') as fi:
#     for i in fi:
#         z.append(i.strip().split(','))
#     if dct.get(z[0]):
#         dct[z[0]] += z
#     else:
#         dct[z[0]] = z



        # for k, v in row.items():
        #     z.append(v)
        # y = z.pop(0)
        # dct[y] = z

# print(dct)
# print(wb.sheetnames)
# wb.save("Task_11-2.xlsx")
