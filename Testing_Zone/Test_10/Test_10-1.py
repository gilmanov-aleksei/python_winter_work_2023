#! /usr/bin/python

lst = [1, 2, 3, 4, 5]
for x in lst:
    lst.pop()
    print(x, lst)

lst1 = [1, 2, 3, 4, 5]
for y in lst1:
    lst1.pop(0)
    print(y, lst1)