#! /usr/bin/python

# задача 27-1
#
# Введите число n от 1 да 18
# Напечатайте квадратную матрицу, имитирующую Дартс.
# Например для n = 5.
# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1

n = 1
while n > 0:
    n = int(input("Введите число n от 1 до 18, 0 - Выход: "))
    if n != 0:
        if n > 18:
            continue
        else:
            print("Вариант 1 - без матрицы\n")
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    val = min(i, j, n - i + 1, n - j + 1)
                    print(val, end=' ')
                print()
            print()
            print("Вариант 2 - с матрицей\n")
            # Создаем матрицу размером n на n и заполняем ее нулями
            matrix = [[0] * n for x in range(n)]
            # Заполняем матрицу цифрами
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    val = min(i, j, n - i + 1, n - j + 1)
                    matrix[i - 1][j - 1] = val
            # Выводим матрицу на экран
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
