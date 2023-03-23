#! /usr/bin/python

# Задача 26-2

# Создайте класс Par, используя функцию type и с методом dis,
# определенную заранее и печатающую все атрибуты класса Par.
# Функцию dis для метода Par.dis определите заранее.


def print_attrs(cls):
    print("Class attributes:")
    for attr in cls.__dict__:
        if not attr.startswith("__"):
            print(attr)


Par = type("Par", (), {"dis": print_attrs})

print(Par().dis())
