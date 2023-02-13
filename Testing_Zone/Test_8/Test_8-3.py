#! /usr/bin/python

import calendar

year, month = tuple(map(int, input().split()))
print(calendar.month(year, month))
