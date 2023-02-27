#! /usr/bin/python

# Создайте декоратор, который переводит все
# текстовые аргументы функции в верхний регистр
# и возвращаетих в виде списка текстовых аргументов.


def fu(*args, **kwargs):
    res = []
    for x in args:
        if type(x) == str:
            res.append(x)
    for x in kwargs:
        if type(kwargs[x]) == str:
            res.append(kwargs[x])
    return [y.upper() for y in res]


print(fu(1, 2, 'abc', a=3, b='def'))
