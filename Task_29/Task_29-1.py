#! /usr/bin/python

# Задача 29-1

# Дан список, который состоит из одинаковых чисел за исключаением одного.
# Найдите это число.


lst = [11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 11, 11, 11, 11]
print("".join(map(str, [num for num in lst if lst.count(num) == 1])))

# for num in lst:
#     if lst.count(num) == 1:
#         print("Искомое число:", num)
# num for num in lst if lst.count(num) == 1

# lst = [11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 11, 11, 11, 11]
# dct = {}
# for elem in lst:
#     dct[elem] = dct.get(elem, 0) + 1
# for key, value in dct.items():
#     if value == 1:
#         print("Искомое число:", key)
