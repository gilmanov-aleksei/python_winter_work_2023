#! /usr/bin/python

# Создайте функцию, навход которой подается список из целых
# положительных чисел, и которая в качестве результата
# возвращает самое большое число, которое можно составитьиз этих чисел.
# Напиример, вход [1, 21, 3], результат 3211
# Если вход [9, 81, 25], то результат 98125


# Рабочий вариант, разложенный и расписанный
# def max_number(num):
#     # Преобразуем список чисел в список строк
#     num = [str(x) for x in num]
#     # Обеденим строки в одну (получим одну цифру)
#     num = ''.join(num)
#     # Сортируем цифры в убывающем порядке
#     num = sorted(num, reverse=True)
#     # Обеденим строки в одну (получим одну цифру)
#     return ''.join(num)


def max_number(num):
    return ''.join(sorted(''.join([str(x) for x in num]), reverse=True))


numbers = [9, 81, 25, 4, 87, 9]
print(*numbers)
print(max_number(numbers))
