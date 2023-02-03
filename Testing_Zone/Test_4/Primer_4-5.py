#! /usr/bin/python

lst = [123, 234, 345, 456]
sum_dig = lambda x: sum(map(int, str(x)))
print(list(map(sum_dig, lst)))
