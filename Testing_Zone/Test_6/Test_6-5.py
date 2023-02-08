#! /usr/bin/python

import openpyxl
# from openpyxl import Workbook
wb = openpyxl.load_workbook("test.xlsx")
wb.save('test.xlsx')
ws = wb.active
wb.active = ws
print(ws.title)
print(wb.sheetnames)
wb.create_sheet("Newssheet")


#
