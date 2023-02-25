#! /usr/bin/python

# def null_decorator(func):
#     return func  # Возвращает саму функцию
#
#
# def hello():
#     print('Hello world!')
#
#
# hello = null_decorator(hello)  # декорируем функцию hello
# hello()

# def sample_decorator(func):  # определяем декоратор
#     def wrapper():
#         print('Начало функции')
#         func()
#         # мы обертываем функцию func , не вмешиваясь
#         # в ее работу
#         print('Конец функции')
#
#     return wrapper
#
#
# def say():
#     print('Привет Мир!')
#
#
# say = sample_decorator(say)  # декорируем функцию
# say()  # вызываем декорированную функцию

def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

# @uppercase_decorator
def h():
    return 'Hello'

# h = uppercase_decorator(h)
print(h())
