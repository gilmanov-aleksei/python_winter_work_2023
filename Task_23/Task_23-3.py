#! /usr/bin/python

# Создайте функцию, на вход которой подается список из целых
# положительных чисел, и которая в качестве результата
# возвращает самое большое число, которое можно составитьиз этих чисел.
# Напиример, вход [1, 21, 3], результат 3211
# Если вход [9, 81, 25], то результат 98125


import itertools


def max_number(num):
    # Список чисел, переведем в список строк
    num = [str(n) for n in num]
    # Перемешаем строки с помощью itertools
    combinations = list(itertools.permutations(num))
    # Полученый список картежей переведем в список строк
    lst = [''.join(c) for c in combinations]
    # Сортируем список по возрастанию
    lst.sort()
    # Последний элемент списка, это наибольшее число
    big_num = lst.pop()
    return big_num


numbers = [1, 21, 3]
print(max_number(numbers))

numbers = [9, 81, 25]
print(max_number(numbers))

# def max_number(numbers):
#     # сортируем числа по убыванию
#     numbers = ''.join(str(n) for n in numbers)
#     # объединяем число в порядке убывания
#     largest = ''.join(sorted(numbers, reverse=True))
#     return largest

# def max_number(num):
#     # Преобразуем каждое число в строку, чтобы можно было сравнивать цифры
#     num = [str(n) for n in num]
#     # Сортируем список по убыванию, используя лексикографический порядок строк
#     num.sort(reverse=True)
#     # Объединяем отсортированные числа в одну строку и преобразуем обратно в число
#     largest = int(''.join(num))
#     return largest

# def max_number(num):
#     # Функция для сравнения чисел
#     def compare(a, b):
#         return int(b + a) - int(a + b)
#     # Преобразуем каждое число в строку, чтобы можно было сравнивать цифры
#     num = [str(n) for n in num]
#     # Сортируем список по убыванию, используя кастомную функцию сравнения
#     num.sort(key=cmp_to_key(compare))
#     # Объединяем отсортированные числа в одну строку и преобразуем обратно в число
#     largest = int(''.join(num))
#     return largest
