#! /usr/bin/python

# Задача 29-1

# Дан список, который состоит из одинаковых чисел за исключаением одного.
# Найдите это число.


lst = [11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 11, 11, 11, 11, 11]
print("Искомое число:", "".join(map(str, [num for num in lst if lst.count(num) == 1])))

for num in lst:
    if lst.count(num) == 1:
        print("Искомое число:", num)

dct = {}
for i in lst:
    dct[i] = dct.get(i, 0) + 1
print("Искомое число:", *[k for k, v in dct.items() if v == 1])
# for k, v in dct.items():
#     if v == 1:
#         print("Искомое число:", k)
