#! /usr/bin/python

def fn01(x):
    return 0   if x == 1 else 1

x = 0
for _ in range(10):
    print(x := fn01(x))