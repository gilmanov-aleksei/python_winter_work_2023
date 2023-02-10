#! /usr/bin/python

import calendar

year = int(input('Введите номер года: '))
dw = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for month in range(1, 13):
   for day in range(1, calendar.monthrange(year, month)[1] + 1):
       dd = calendar.weekday(year, month, day)
       # dw[dd] += 1
       dw[dd] = dw.get(dd, 0) + 1
print(dw)
