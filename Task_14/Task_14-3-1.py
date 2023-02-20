#! /usr/bin/python

# Задача 14-3-1
# Напишите рекурсивную функцию romb(n),
# которая печатает два треугольника?  в форме ромба
# Например, для n = 5:
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

def romb1(n, m=0):
    if n == 0:
        print(("* " * m).center(10))
    else:
        print(("* " * m).center(10))
        romb1(n - 1, m + 1)
        print(("* " * m).center(10))
    return


romb1(5)


def romb2(m, n=0):
    if n < m:
        print(' ' * (m - n), '* ' * n)
        romb2(m, n + 1)
    print(' ' * (m - n), '* ' * n)
    return


romb2(5)
