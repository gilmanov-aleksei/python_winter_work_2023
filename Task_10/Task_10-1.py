#! /usr/bin/python

import openpyxl

wb = openpyxl.load_workbook("task_10-1.xlsx")
str = wb.sheetnames
ws = wb[str[0]]
print(ws.title)
d ={}
for i in range(ws.max_row):
    fio = ''
    zp = []
    for j in range(ws.max_column):
        if j != 0:
            zp.append(ws.cell(row=i + 1, column=j + 1).value)
        else:
            fio = ws.cell(row=i + 1, column=j + 1).value
    d[fio] = zp
print(d)
# ws = wb[str[1]]
# print(ws.title)
# c = ws['A1']
# print(c.coordinate, c.value)
for k, v in d.items():
    print(k, sum(v))
