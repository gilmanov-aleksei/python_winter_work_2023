#! /usr/bin/python

import datetime, locale

import calendar

year = tuple(map(int, input().split()))
print(calendar.calendar(year))


locale.setlocale(locale.LC_ALL, 'ru')
a = datetime.datetime.today() + datetime.timedelta(days=14)
print(a)
c = datetime.timedelta(days=1)
for _ in range(10):
    a += c
    print(a.strftime('%A %d, %B %Y'), "-", a)
