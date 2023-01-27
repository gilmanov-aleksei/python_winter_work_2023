#! /usr/bin/python

n = int(input('Введите число: '))

# Создаем список с 0 значениями в n-ячеек
mas = [[0] * n for i in range(n)]

# Значение индекса для ячеек
num = 1
# Текущее положение ячейки X
x = 0
# Текущее положение ячейки Y
y = -1
# Движение по рядам -1-движение верх по ряду 0-остаёмс в том же ряду 1-движение вниз по ряду
mas_row = 0
# Движение по колонке -1-движение влево по строке 0-остаёмс на той же строке 1-движение вправо по строке
mas_col = 1
# Повторять цикл пока значение ячейки меньше n ^ 2
while num <= n * n:
    # Проверяем, ячека ровна нулю и не выходит ячейки за пределы списка
    if mas[x+mas_row][y+mas_col] == 0 <= x+mas_row < n and 0 <= y+mas_col < n:
        # Если не выходит и ровна 0, то записываем значения
        # Записываем занчение ряда в X
        x += mas_row
        # Записываем значение строки в Y
        y += mas_col
        # Записываем значения индекса в ячеку
        mas[x][y] = num
        # Увеличиваем индекс на 1
        num += 1
        # Иначе, меняем движение по условию
    else:
        # Если двигались вправо, то строка на месте, по ряду двигаемся вниз
        if mas_col == 1:
            mas_col = 0
            mas_row = 1
        # Если двигались вниз, то по строке двигаемся влево, по ряду на месте
        elif mas_row == 1:
            mas_col = -1
            mas_row = 0
        # Если двигались влево, то строка на месте, по ряду двиагемся вверх
        elif mas_col == -1:
            mas_col = 0
            mas_row = -1
        # Если двигались вверх, то по строке двигаемся в право, по ряду на месте
        elif mas_row == -1:
            mas_col = 1
            mas_row = 0
# Выводим результат на печать
for row in mas:
    # Печатаем построчно элементы списка
    for element in row:
        # Переобразуем элемент в строку
        # и вырвним по правому краю строку по ширине,
        # без переноса на новую строку
        print(str(element).rjust(len(str(n * n))), end=' ')
    # Печатаем пустую строку
    print()
