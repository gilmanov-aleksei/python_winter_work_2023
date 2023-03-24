#! /usr/bin/python

# Задача 26-2

# Создайте класс Par, используя функцию type и с методом dis,
# определенную заранее и печатающую все атрибуты класса Par.
# Функцию dis для метода Par.dis определите заранее.


def dis(obj):
    # print(Par.__dict__)
    print(f"All attributes of {obj.__class__.__name__}:")
    print(dir(obj))


Par = type('Par', (), {'dis': dis, 'x':123})

Par().dis()
