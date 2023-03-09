#! /usr/bin/python

# Задача 16-3
# Создайте декоратор, который переводит все слова к следующему виду,
# первая буква в верхнем регистре, а остальные в нижнем.

def fun1(text):
    def fun2(t):
        return t.title()

    return fun2(text)


print(fun1('hEllO, wORLd! пРиВеТ, мИр!'))
