#! /usr/bin/python

import time

y = 1000000000
t0 = time.time()
s = []
for i in range(y):
    s.append(i ** 3)
t1 = time.time()
a = list(map(lambda x: x ** 3, range(y)))
t2 = time.time()
b = [x ** 3 for x in range(y)]
t3 = time.time()
print(t1 - t0)
print(t2 - t1)
print(t3 - t2)



def fn01(x):
    return 0   if x == 1 else 1

x = 0
for _ in range(10):
    print(x := fn01(x))