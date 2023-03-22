#! /usr/bin/python

# class Anyclass:
#     def __init__(self, x, y):
#         self.x = x
#         self.__y = y
#
# any = Anyclass(123, 456)
# print(any.x)
# print(any.__y)
# print(any._Anyclass__y)

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1
#
#     def set_age(self, age):
#         if 1 < age < 10:
#             self.__age = age
#         else:
#             print("Недопусимый возраст")
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Имя: {self.__name} Возраст: {self.__age}")
#
# tom = Person("Tom")
# tom.display_info()
# tom.set_age(25)
# tom.display_info()

class Foo(object):
    bar = True
Foo1 = type('Foo1', (), {'bar': True})
Foo1Child = type('Foo1Child', (Foo1,), {})

def echo_bar(self):
    print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

print(hasattr(FooChild, 'echo_bar'))

my_foo = FooChild()
my_foo.echo_bar()
my_foo.bar = 123
my_foo.echo_bar()
print(FooChild.__dict__)