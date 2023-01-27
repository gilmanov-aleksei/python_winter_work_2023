#! /usr/bin/python

# n = int(input('Введите число: '))
n = 3
d = {}
num = 1
x = 0
y = -1
d_row = 0
d_cow = 1

for i in range(1, n * n + 1):
    d[i] = d.get((x,y), -1)
print(d)

# d[i] = d.get((x,y), -1)
# print(d)
# d[i] = d[i] - 1
