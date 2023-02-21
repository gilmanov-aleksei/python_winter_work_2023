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
# import openpyxl

with open('Task_11-2.csv') as f:
    reader = list(csv.reader(f, delimiter=','))
    begin = reader.pop(0)
    print(*begin)
    print()
    reader.sort(key=lambda x: [x[3], x[1], x[2]])
    for row in reader:
        for txt in row:
            print(txt, end=" ")
        print()

# wb = openpyxl.Workbook()
# sheet = wb.sheetnames
# wb.create_sheet("Лист1")
# ws = wb[sheet[0]]
# print(sheet)
# print(ws.title)
# wb.save("Task_11-2.xlsx")
