#! /usr/bin/python

import calendar

year = tuple(map(int, input().split()))
print(calendar.calendar(year))