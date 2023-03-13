#! /usr/bin/python

# Задача 21-2
# Напишите функцию, которая находит оптимальный маршрут из верхнего
# левого угла в правый нижний угол матрицы. Двигаться можно только вправо
# или вниз. В каждой клетке матрице содержится число. Оптимальным
# считается маршрут с минимальной суммой чисел клеток, через которые
# проходит маршрут.
#
# Например, если матрица 3 х 3 :
# [[10,20,30], [5,1,80], [90,2,70]], то оптимальным будем маршрут,
# который проходит через клетки 10 + 5 + 1 + 2 + 70 = 88.
# Подсказка: полный перебор вариантов заведомо неэффективен.
# Возможное решение идти от начала и запоминать оптимальные маршруты
# для каждой клетки из начала.


from random import randint


def random_matrix():
    rows = int(input("Введите количество строк в матрице: "))
    cols = int(input("Введите количество столбцов в матрице: "))
    # Создание двумерной матрицы
    m = [[0 for _ in range(cols)] for _ in range(rows)]
    # Заполнение матрицы случайными числами от 1 до 99
    for row in range(rows):
        r1 = randint(1, 9)
        for col in range(cols):
            r2 = randint(10, 99)
            m[row][col] = randint(r1, r2)
    return m


def print_matrix(m):
    # определяем максимальное количество символов в строке
    max_len = len(str(max([max(row) for row in m])))
    # выводим матрицу на экран
    for row in m:
        for item in row:
            # форматируем каждый элемент, выравнивая по максимальному количеству символов
            print(f"{item:>{max_len}}".format(item=item, max_len=max_len), end=" ")
        # переходим на новую строку
        print()
    return


def backtracking(a, b, m1, m2):
    # Найдем путь с помощью бэктрекинга
    # (алгоритм из интернета, запись индекса и значения ячейки)
    i, j = a - 1, b - 1
    # Список для сбора значений по движению в матрице
    path_num = []
    # Список для сбора индексов по движению в матрице
    # с записью максимального индекса
    path_index = [(i, j)]
    # Цикл в матрице, пока она не закончиться,
    # то есть не выйдем за её пределы
    while i >= 0 and j >= 0:
        # Сохраняем в список значение из ячеки
        path_num.append(m1[i][j])
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if m2[i - 1][j] < m2[i][j - 1]:
                i -= 1
            else:
                j -= 1
        # Сохраняем в список индекс ячейки
        path_index.append((i, j))
        # Удаляем последнее значение индекса из списка,
    # так как оно находиться за пределами матрицы
    path_index.pop()
    # Переворачиваем список значений
    path_num.reverse()
    # Переворачиваем список индексов с выводом на экран
    print("Маршрут по ячейкам: (строка, колонка)")
    print(*path_index[::-1])
    # Вывод значений на экран
    print("Маршрут по значениям: ", *path_num)
    return m2[a - 1][b - 1]


# Функция поиска оптимального маршрута в матрице
def find_optimal_route_matrix(form, pr=0):
    # Узнаём количество строк в матрице
    m = len(form)
    # Узнаём количество столбцов в первой строке матрицы
    n = len(form[0])
    # Создаём матрицу для посчета маршрута с заполнением её 0 значениями
    dp = [[0] * n for _ in range(m)]
    # Найдем сумму чисел на пути вдоль первой колонки
    for i in range(m):
        if i == 0:
            dp[i][0] = form[i][0]
        else:
            dp[i][0] = dp[i - 1][0] + form[i][0]
    # Найдем сумму чисел на пути вдоль первой строки
    for j in range(n):
        if j == 0:
            dp[0][j] = form[0][j]
        else:
            dp[0][j] = dp[0][j - 1] + form[0][j]
    # Найдем оптимальный маршрут заполнив оставшиеся ячейки
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + form[i][j]
    if pr == 1:
        return backtracking(m, n, form, dp)
    else:
        return dp[m - 1][n - 1]


matrix = [[10, 20, 30], [5, 1, 80], [90, 2, 70]]
# Генерация матрицы
# matrix = random_matrix()
# Выводит на экран матрицу
print_matrix(matrix)
# 1 - выводить на экран маршрут движения по матрице, 0 - нет
p_route = 1
result = find_optimal_route_matrix(matrix, p_route)
print("Сумма наименьшего маршрута: ", result)
