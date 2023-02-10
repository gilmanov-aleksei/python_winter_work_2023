#! /usr/bin/python

import openpyxl
from random import randint
from russian_names import RussianNames


def gen_fio_sheet(s, fio, name_file):
    # Генератор русских фамилий, имён и отчества русскими буквами
    rn = RussianNames(count=fio, patronymic=False, name=False, surname=True)
    wb = openpyxl.load_workbook(name_file)
    sheets = wb.sheetnames
    ws = wb[sheets[s]]
    fio = rn.get_batch()
    for v, k in enumerate(fio, 1):
        ws['A' + str(v)] = k
    for i in range(66, 76):
        for j in range(1, ws.max_row + 1):
            ws[str(chr(i)) + str(j)] = int(randint(0, 9))
    wb.save(name_file)
    return


# Генератор фамилий и 5 колонок значений,
# первый аргумент - это номер листа,
# второй аргумент - это колличество фамилий
# третий аргумент - это имя файла, для сохранения результата
gen_fio_sheet(0, 15, "task_10-3.xlsx")
