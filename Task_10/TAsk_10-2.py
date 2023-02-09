#! /usr/bin/python

# Импортируем модуль openpyxl
import openpyxl

# gen_fio_sheet(1, 15)


wb = openpyxl.load_workbook("task_10-2.xlsx")
sheets = wb.sheetnames
# ws = wb[sheets[s]]
# wb.active = sheet
