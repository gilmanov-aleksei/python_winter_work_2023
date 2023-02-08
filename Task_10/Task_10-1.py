#! /usr/bin/python

import openpyxl
mr = 0
mc = 0
fio = ''
d ={}

wb = openpyxl.load_workbook("task_10-1.xlsx")
str = wb.sheetnames
print(str)
ws = wb[str[0]]
print(ws.title)
for i in range(ws.max_row):
    zp = []
    for j in range(ws.max_column):
        if j != 0:
            zp.append(ws.cell(row=i + 1, column=j + 1).value)
        else:
            fio = ws.cell(row=i + 1, column=j + 1).value
    d.setdefault(fio, zp)
print(d)
ws = wb[str[1]]
print(ws.title)
