#! /usr/bin/python

# Задача 29-2

# Дана квадратная матрица, напишите функцию, которая возвращает матрицу,
# полученную вращением по или против часовой стрелке.
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# rotate(matrix, "по часовой") # -----> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

def rotate(matrix):
    len_m = len(matrix)
    rotated_m = []
    for j in range(len_m):
        row = []
        for i in range(len_m - 1, -1, -1):
            row.append(matrix[i][j])
        rotated_m.append(row)
    return rotated_m


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))  # -----> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
