#! /usr/bin/python

# Импортируем модуль openpyxl
import openpyxl
wb = openpyxl.load_workbook("task_10-2.xlsx")
sheets = wb.sheetnames

# ws = wb[sheets[s]]
# wb.active = sheet
