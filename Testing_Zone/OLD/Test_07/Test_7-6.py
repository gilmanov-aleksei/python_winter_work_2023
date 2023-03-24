#! /usr/bin/python

#import datetime package
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru')

today = datetime.datetime.now()
print(datetime.datetime.strftime(today, '%d %B'))
