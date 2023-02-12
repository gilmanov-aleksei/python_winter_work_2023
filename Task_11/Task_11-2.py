#! /usr/bin/python

# Задача 11-2
#  - Дан файл с расширением .csv ,
#  содержащий в каждой строчке следующую информацию:
#  номер, фамилия, имя, компания, зарплата.
#  - Создайте Эксельный файл, в который перенесите эту информацию,
#  предварительно отсортировав этот список по компании, по фамилии и имени.
#  - В конце списка добавьте строку: ИТОГО и суммарное значение всех зарплат.

# Импортируем модуль openpyxl
import openpyxl
import csv

d = {}
# reader = {}
# print(d)
with open('test_11-2.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


# wb = openpyxl.load_workbook("test_11-2.xlsx")
# for sh in wb.sheetnames:
#      ws = wb[sh]
#      print(ws.title, '-------')
    # for i in range(ws.max_row):
    #     for j in range(ws.max_column):
    #         print(i + 1, j + 1, ws.cell(i + 1, j + 1).value)
    # ws = wb[sh]

# wb.save("test_11-2.xlsx")
