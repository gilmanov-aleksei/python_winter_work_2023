#! /usr/bin/python

import datetime, locale

locale.setlocale(locale.LC_ALL, 'ru')
a = datetime.datetime.today() + datetime.timedelta(days=14)
print(a)
c = datetime.timedelta(days=1)
for _ in range(10):
    a += c
    print(a.strftime('%A %d, %B %Y'), "-", a)
