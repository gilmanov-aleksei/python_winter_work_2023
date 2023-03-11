#! /usr/bin/python


def find_min_route(matrix):
    m = len(matrix)
    n = len(matrix[0])
    # инициализируем матрицу длин минимальных путей
    path_lens = [[0] * n for i in range(m)]
    # заполняем первую строку и первый столбец
    path_lens[0][0] = matrix[0][0]
    for i in range(1, m):
        path_lens[i][0] = path_lens[i - 1][0] + matrix[i][0]
    for j in range(1, n):
        path_lens[0][j] = path_lens[0][j - 1] + matrix[0][j]
    # заполняем оставшуюся часть матрицы
    for i in range(1, m):
        for j in range(1, n):
            path_lens[i][j] = matrix[i][j] + min(path_lens[i - 1][j], path_lens[i][j - 1])
    # возвращаем последнее значение из матрицы длин минимальных путей
    return path_lens[m - 1][n - 1]


matrix = [[10, 20, 30], [5, 1, 80], [90, 2, 70]]
min_route = find_min_route(matrix)
print(min_route)
