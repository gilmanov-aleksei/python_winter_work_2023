#! /usr/bin/python

# Задача 13-2
# Создайте функцию-генератор,
# которая создаёт последовательность числовых палиндромов:
# 1 2 3 4 5 6 7 8 9
# 11 22 33 44 55 66 77 88 99
# 101 111 121 131 141 151 161 171 181 191 202 212 ...

# def fu():
# for i in range(1, 200):
#     a = str(i)
#     b = ''
#     for j in range(len(a) - 1, -1, -1):
#         b += a[j]
#     if a == b:
#         print(i, end=" ")

import math
def is_palindrom(purpose):
    for i in range(1,int(math.sqrt(purpose))):
        if purpose % i == 0:
            print(i, purpose//i)
is_palindrom(100)


# gf = fu()
# for i in gf:
#     print(i, end=", ")
#     time.sleep(0.25)