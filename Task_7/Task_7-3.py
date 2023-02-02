#! /usr/bin/python

from random import randint
x = []
z = {0}
n = randint(2, 5)
m = randint(2, 5)
print(n, m)
for i in range(n):
    y = []
    for j in range(m):
        y.append(randint(10, 99))
    x.append(y)
print(x)
for i in range(len(x)):
    z.update(x[i])
z.remove(0)
z = sorted(list(z), reverse=True)
print(z)
