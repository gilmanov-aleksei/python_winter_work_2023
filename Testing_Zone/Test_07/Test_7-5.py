#! /usr/bin/python

import datetime
from datetime import datetime
import datetime
import calendar
import locale
from calendar import Calendar

locale.setlocale(locale.LC_ALL, 'ru')

today = datetime.datetime.now()
print(datetime.datetime.strftime(today, '%d %B'))

year = int(input('Введите номер года: '))

obj1 = calendar.Calendar(firstweekday = 3)

for day in obj1.itermonthdates(year, 1):
    print(day, end=' ')
print()

obj2 = calendar.Calendar()
for day in obj2.itermonthdates(year, 9):
    print(day, end=' ')
print()

for month in range(1, 13):
    print(month)
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        print(calendar.weekday(year, month, day), end=' ')
    input()
    print()
       # dw[dd] = dw.get(dd, 0) + 1
# print(dw)


# now = datetime.now()  # текущие дата и время
# print(now)
# # datetime.datetime(2021, 2, 23, 14, 46, 19, 60107)
# print(datetime.weekday(now))  # день недели в виде числа, понедельник - 0, воскресенье - 6
# print(datetime.isoweekday(now))  # день недели в виде числа, понедельник - 1, воскресенье - 7
