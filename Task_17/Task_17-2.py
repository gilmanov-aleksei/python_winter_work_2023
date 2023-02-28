#! /usr/bin/python

# Создайте декоратор, который переводит все
# текстовые аргументы функции в верхний регистр
# и возвращает их в виде списка текстовых аргументов.


def fu1(*args, **kwargs):
    def fu2(*args, **kwargs):
        res = []
        for x in args:
            if type(x) == str:
                res.append(x)
        for x in kwargs:
            if type(kwargs[x]) == str:
                res.append(kwargs[x])
        return [y.upper() for y in res]
    return fu2(*args, **kwargs)


print(fu1(1, 3, 6, 8, 'qwerty', a=3, b='def', v='test', z='plkm'))

