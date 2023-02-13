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

dct = {}
with open('Task_11-2.csv') as f:
    reader = csv.reader(f, delimiter=' ', quotechar='|')
    # reader = csv.DictReader(f)
    for row in reader:
        read = ','.join(row).split(',')
        dct[read[0]] = [i for i in read[1:]]
print(dct)
wb = openpyxl.Workbook()
wb.create_sheet("Лист1")
ws = wb.active
sheet = wb.sheetnames
ws = wb[sheet[1]]
print(sheet)
print(ws.title)
# wb.save("Task_11-2.xlsx")
