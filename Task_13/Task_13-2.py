#! /usr/bin/python
import time


# Задача 13-2
# Создайте функцию-генератор,
# которая создаёт последовательность числовых палиндромов:
# 1 2 3 4 5 6 7 8 9
# 11 22 33 44 55 66 77 88 99
# 101 111 121 131 141 151 161 171 181 191 202 212 ...

def fu(v):
    for j in range(1, v):
        m = j
        n = 0
        while j > 0:
            n = n * 10 + j % 10
            j = j // 10
        if m == n:
            yield m


gf = fu(250)
for i in gf:
    print(i, end=", ")
    time.sleep(0.25)
