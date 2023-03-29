#! /usr/bin/python

# Задача 29-1

# Дан список, который состоит из одинаковых чисел за исключаением одного.
# Найдите это число.


lst = [11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 11, 11, 11, 11]
print("Исключение:", " ".join(map(str, [num for num in lst if lst.count(num) == 1])))

for num in lst:
    if lst.count(num) == 1:
        print("Исключение:", num)

dct = {}
for d in lst:
    dct[d] = dct.get(d, 0) + 1
print("Исключение:", *[k for k, v in dct.items() if v == 1])
# for k, v in dct.items():
#     if v == 1:
#         print("Искомое число:", k)
