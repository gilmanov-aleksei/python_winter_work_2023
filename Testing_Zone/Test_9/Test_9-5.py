#! /usr/bin/python

def fun(n):
    for x in range(n):
        yield x * x


g = fun(3)
print(next(g))
print(next(g))
print(next(g))
try:
    print(print(next(g)))
except StopIteration:
    print("Больше нет данных")
