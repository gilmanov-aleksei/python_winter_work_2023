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
def romb(m, n=0):
    print(' ' * (m - n), '* ' * n)
    if n < m:
        romb(m, n + 1)
        print(' ' * (m - n), '* ' * n)
    return


romb(7)


def romb1(n, m=0):
    if n == 0:
        print(("* " * m).center(15))
    else:
        print(("* " * m).center(15))
        romb1(n - 1, m + 1)
        print(("* " * m).center(15))
    return


romb1(7)
