#! /usr/bin/python

import calendar

year = tuple(map(int, input().split()))
print(calendar.calendar(year))

print([x ** 2 for x in range(0, 50) if x % 10 == 0])