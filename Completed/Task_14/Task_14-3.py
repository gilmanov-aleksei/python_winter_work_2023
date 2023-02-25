#! /usr/bin/python

# Задача 14-3
# Напишите рекурсивную функцию tri_2(n),
# которая печатает два треугольника.
# Например, для n = 5:
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# Подсказака: одна строка печатается до вызова функции,
# а вторая после вызова


def tri_2_1(n, m=0):
    if n > 1:
        print(' ' * m, '* ' * n)
        tri_2_1(n - 1, m + 1)
    print(' ' * m, '* ' * n)
    return


def tri_2_2(n, m=0):
    if n > 1:
        if n % 2 != 0:
            print(' ' * m, '* ' * n)
        tri_2_2(n - 1, m + 1)
    if n % 2 != 0:
        print(' ' * m, '* ' * n)
    return


tri_2_1(int(input("Enter the number: ")))
print()
tri_2_2(int(input("Enter the number: ")))
