#! /usr/bin/python

n = 5
m = 6
mas = {(x, y): 0 for x, y in range(n+1)}
print(mas)

lst = [[ i * j for j in range(m)] for i in range(n)]
print(lst, end=' ')
d = {a: a ** 2 for a in range(7)}