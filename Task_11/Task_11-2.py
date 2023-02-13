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
import openpyxl

row = {}
dct = {}
srt = ""
wb = openpyxl.Workbook()
with open('Task_11-2.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        z = []
        print(row)
        for k, v in row.items():
            z.append(v)
        y = z.pop(0)
        dct[y] = z

print(dct)
print(wb.sheetnames)
wb.save("Task_11-2.xlsx")
