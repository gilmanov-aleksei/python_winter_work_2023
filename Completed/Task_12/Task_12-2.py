#! /usr/bin/python

# Задача 12-2
# Создайте списковое включение ,
# которое генерирует следующую последовательность:
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10

print(*[x for x in range(1, 11) for y in range(x)])

# Пустой списолк
# lst = []
# #Цикл от 1 до 10 включительно
# for x in range(1, 11):
#     # Цикл от 0 до Х
#     for y in range(x):
#         # Прибавляем Х к списку
#         lst.append(x)
# Вывод на экран списка
# print(*lst)