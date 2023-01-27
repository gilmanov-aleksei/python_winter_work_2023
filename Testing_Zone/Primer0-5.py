#! /usr/bin/python

# n = int(input('Введите число: '))
n = 3
d = {}
num = 1
x = 1
y = 1
d_row = 0
d_col = 0

#     if 0 <= x + mas_row < n and 0 <= y + mas_col < n and mas[x + mas_row][y + mas_col] == 0:
while num <= n * n:
    d[num] = d.get(num, (x, y))
    x += d_row
    y += d_col
    num += 1

print(d)

