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


romb(int(input("Enter the number: ")))
