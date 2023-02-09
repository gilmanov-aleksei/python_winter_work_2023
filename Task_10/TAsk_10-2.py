#! /usr/bin/python

# Импортируем модуль openpyxl
import openpyxl
from russian_names import RussianNames

rn = RussianNames(count=10, patronymic=False, name=False, surname=True)
fio = rn.get_batch()
print(fio)

wb = openpyxl.load_workbook("task_10-2.xlsx")
sheet = wb.sheetnames
ws = wb[sheet[0]]