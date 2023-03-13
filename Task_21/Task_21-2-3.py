#! /usr/bin/python


def print_matrix(m1):
    # определяем максимальное количество символов в строке
    max_len = len(str(max([max(row) for row in m1])))
    # выводим матрицу на экран
    for row in m1:
        for item in row:
            # форматируем каmatrixждый элемент, выравнивая по максимальному количеству символов
            print(f"{item:>{max_len}}".format(item=item, max_len=max_len), end=" ")
        # переходим на новую строку
        print()
    return


def backtracking(m2, i, j):
    # Найдем путь с помощью бэктрекинга
    # Список для сбора значений по движению в матрице
    path_num = []
    # Список для сбора индексов по движению в матрице
    path_index = [(i, j)]
    # Цикл в матрице, пока она не закончиться,
    # то есть не выйдем за её пределы
    while i >= 0 and j >= 0:
        # Сохраняем в список значение из ячеки
        path_num.append(m2[i][j])
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
    return sum(path_num)


mat_rix = [[10, 3, 20, 30], [5, 10, 1, 80], [90, 5, 2, 70]]
m = len(mat_rix)
n = len(mat_rix[0])
print_matrix(mat_rix)
bt = backtracking(mat_rix, m - 1, n - 1)
print("Сумма наименьшего маршрута: ", bt)
