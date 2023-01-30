#! /usr/bin/python

month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30,12:31}

while True:
    y, m = int(input()), int(input())
    if y == 0 and m == 0:
        break
    if y % 4 == 0 and m == 2:
        print('29')
    else:
        print(month[m])

