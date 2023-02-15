#! /usr/bin/python

# Задача 11-1
# - Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# - Напечатайте список дат в 2023 году, когда вход бесплатен.

import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru')

print('Эрмитаж, бесплатные дни на 2023 год')

year = 2023
for month in range(1, 13):
    c = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        if calendar.weekday(year, month, day) == 3:
            c += 1
            if c == 3:
                print(datetime.date(year, month, day).strftime("%d %b"), end='. ')
