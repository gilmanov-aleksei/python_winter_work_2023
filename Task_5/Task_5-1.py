#! /usr/bin/python

n = int(input("Введите число: "))
# Пустой список
lst = []
# Цикл пока n не равно нулю
while n != 0:
    # Записываем 1 в первый индекс списка
    # и прибавляем к нему текущий список
    lst = [1] + lst
    # Цикл на длину списка - 1 начиная со второго элемента
    for i in range(1, len(lst) - 1):
        # Записываем в список значение из текущей ячеки
        # прибавля её со следующим заначением ячейки
        lst[i] += lst[i + 1]
    # Печатем полученый список с отступом
    # от левого края на n пробелов
    print(" " * n, *lst)
    n -= 1
