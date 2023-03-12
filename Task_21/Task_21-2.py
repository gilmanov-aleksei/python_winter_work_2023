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
    m = [[0 for x in range(cols)] for y in range(rows)]
    # Заполнение матрицы случайными числами от 1 до 99
    for row in range(rows):
        r1 = randint(1, 9)
        for col in range(cols):
            r2 = randint(10, 99)
            m[row][col] = randint(r1, r2)
    return m


# Функция поиска оптимального маршрута в матрице
def find_optimal_route_matrix(form):
    # Узнаём количество строк в матрице
    m = len(form)
    # Узнаём количество столбцов в первой строке матрицы
    n = len(form[0])
    # Создаём матрицу со знаечниями 0
    dp = [[0] * n for _ in range(m)]
    # Найдем сумму чисел на пути вдоль первой колонки
    for i in range(m):
        dp[i][0] = form[i][0] if i == 0 else dp[i - 1][0] + form[i][0]
    # Найдем сумму чисел на пути вдоль первой строки
    for j in range(n):
        dp[0][j] = form[0][j] if j == 0 else dp[0][j - 1] + form[0][j]
    # Найдем оптимальный маршрут заполнив оставшиеся ячейки
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + form[i][j]
    # Найдем путь с помощью бэктрекинга
    # (алгоритм из интернета, алгоритмы запись индекса и значения ячейки)
    i, j = m - 1, n - 1
    # Список для сбора значений по движению в матрице
    path_num = []
    # Список для сбора индексов по движению в матрице
    path_index = []
    # Цикл в матрице, пока она не закончиться,
    # то есть не выйдем за её пределы
    while i >= 0 and j >= 0:
        # Сохраняем в список значение из ячеки
        path_num.append(form[i][j])
        # Сохраняем в список индекс ячейки
        # path_index.append((i, j))
        path_index.append((i + 1, j + 1))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
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
    return dp[m - 1][n - 1]


matrix = [[10, 20, 30], [5, 1, 80], [90, 2, 70]]
# matrix = random_matrix()
# определяем максимальное количество символов в строке
max_len = len(str(max([max(row) for row in matrix])))
# выводим матрицу на экран
print("Матрица")
for row in matrix:
    for item in row:
        # форматируем каждый элемент, выравнивая по максимальному количеству символов
        print(f"{item:>{max_len}}".format(item=item, max_len=max_len), end=" ")
    # переходим на новую строку
    print()

result = find_optimal_route_matrix(matrix)
print("Сумма наименьшего маршрута: ", result)
