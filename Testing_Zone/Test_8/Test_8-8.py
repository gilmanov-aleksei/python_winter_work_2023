#! /usr/bin/python

import datetime
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'ru')


year, month = map(int, input().split())
a = calendar.monthrange(year,month)
s = [(i + 1, month, year) for i in range(a[1])]
print(*s)
# def year_mon(y,m):
#     return [[y for m in range(1, 13)] for d in range(1, calendar.monthrange(y, m)[1] + 1)]
#
# print(year_mon(2023, 2))
#
# calendar.monthrange()
# # year = 2023
# for month in range(1, 13):
#     for day in range(1, calendar.monthrange(year, month)[1] + 1):
#         dd = calendar.weekday(year, month, day)
