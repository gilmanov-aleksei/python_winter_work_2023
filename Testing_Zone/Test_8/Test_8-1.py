#! /usr/bin/python

a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]

c = [1, 2, 3, 4]
d = c
c += [5, 6, 7, 8]

print(a, b)
print(c, d)
