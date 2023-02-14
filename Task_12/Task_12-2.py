#! /usr/bin/python

# Задача 12-2
# Создайте списковое включение ,
# которое генерирует следующую последовательность:
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10

lst = [x for x in range(1, 11) for y in range(x)]
# lst = []
# for i in range(1, 11):
#     for j in range(i):
#         lst.append(i)
print(lst)
