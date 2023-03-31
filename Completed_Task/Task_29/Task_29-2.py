#! /usr/bin/python

# Задача 29-2

# Дана квадратная матрица, напишите функцию, которая возвращает матрицу,
# полученную вращением по или против часовой стрелке.
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# rotate(matrix, "по часовой") # -----> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

def rotate1(m):
    # Пустой список, для новой матрицы
    rotated_m = []
    # Цикл по всей длине матрицы
    for i in range(len(m)):
        # Пустой список, для новой строки матрицы
        row_m = []
        for j in range(len(m) - 1, -1, -1):
            # Добавляем элемент матрицы вновую строку
            row_m.append(m[j][i])
        # Добавляем новую строку в новую матрицу
        rotated_m.append(row_m)
    return rotated_m


def rotate2(m):
    # Пустой список, для новой матрицы
    rotated_m = []
    for j in range(len(m) - 1, -1, -1):
        # Пустой список, для новой строки матрицы
        row_m = []
        for i in range(len(m)):
            # Добавляем элемент матрицы вновую строку
            row_m.append(m[i][j])
        # Добавляем новую строку в новую матрицу
        rotated_m.append(row_m)
    return rotated_m


def print_matrix(pm):
    for row in pm:
        for col in row:
            print(col, end=' ')
        print()
    print()
    return


print("Вращение матрицы по часовой стрелке")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for _ in range(4):
    print_matrix(matrix)
    matrix = rotate1(matrix)

print("Вращение матрицы против часовой стрелки")
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for _ in range(4):
    print_matrix(matrix2)
    matrix2 = rotate2(matrix2)
