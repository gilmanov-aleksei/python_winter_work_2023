#! /usr/bin/python

# Здача 15-1
# Создайте рекурсивную функцию, которая получаеткак аргумент dct словарь,
# который может содержать словари, которые могут содержатьсловари и т.д. и
# как аргумент х значение ключа.
# Например:
# dct = {1:1, 2:2, {2:22, {1:111, 2:222, {0:1111, 1:2222, 2: 3333}, 1:333}, 1:11,}, 6:22}
# x = 1
# Функция должна составить список, состоящий из значенийсловаря с ключем х.
# Например:
# [1,111,2222,333,11]

def find_key(d, x=1):
    # print(d)
    # Перебираем ключи и значение словаря
    for k, v in d.items():
        # Сравниваем ключ словаря с нашим ключом
        if k == x:
            # если совподает, то проверяем тип значения
            if type(v) == dict:
                # если тип словарь, то реукрсией проеряем его
                find_key(v)
            else:
                # если нет, записываем значение в список
                res.append(d[k])
        else:
            # Если значение не по ключу, то проверяем тип значения
            if type(v) == dict:
                # если тип словарь, то реукрсией проеряем его
                find_key(v)
    # print(res)
    return res


# dct = {1: 1, 2: 2, 6: 22, {2: 22, 1:11, {1: 111, 2: 222, 3:333, {0: 1111, 1: 2222, 2: 3333}}}}
dct = {1: 1, 2: 2, 6: {2: 22, 1: 33, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}}}
res = []
# x = 1
print(dct)
print(find_key(dct))
