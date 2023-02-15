# ! /usr/bin/python
#
print(ord("B"))
print(chr(66))
for i in range(67, 71):
    print(chr(i))

# sheet1 = wb['Sheet1']
# ws = sheet1
# print(ws.title, ws.max_row * ws.max_column)
# sheet2 = wb['Sheet2']
# ws = sheet2
# print(ws.title, ws.max_row * ws.max_column)
# sheet3 = wb['Sheet3']
# ws = sheet3
# print(ws.title, ws.max_row * ws.max_column)
#
# for i in range(ws.max_row):
#     for j in range(ws.max_column):
#
#
# wb.sheetnames
# for sheet in wb:
#     print(sheet.title)
#
#
# sheet = wb['Sheet1']
# wb.active = sheet
# ws['A4'].value = 1234
# c = ws['A4']
# print(c.coordinate, c.value)
# c.value = c.value * 2
# print(ws.max_row)
# for i in range(ws.max_row):
#     for j in range(ws.max_column):
#         print(i + 1, j + 1, ws.cell(row=i + 1, column=j + 1).value)
#
# wb.create_sheet("Sheet1")
# ws = wb.active
# print(ws)
# wb.active = ws
# print(ws.title)
#
# wb.create_sheet("Newssheet")
# wb.save('task_10-0.xlsx')
