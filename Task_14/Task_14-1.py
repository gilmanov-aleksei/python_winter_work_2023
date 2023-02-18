#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет количество
# цифры введенного натурального числа

# def col_num(n):
#     if n < 10:
#         return 1
#     else:
#         pass
#     return
#
#
# print(col_num(int(input("Enter num: "))))


def count_even_odd(n):
    # на случай, если изначально n - отрицательное число
    n = abs(n)
    # если n чётное - последняя цифра тоже чётная
    result = (1, 0) # if n % 2 == 0 else (0, 1)
    # если n сотоит из одной цифры - прерываем рекурсию
    if n < 10:
        return result
    # иначе - отрезаем от n последнюю цифру,
    # вызываем функцию рекурсивно и суммируем результат
    return tuple(map(sum, zip(count_even_odd(n // 10), result)))


print(count_even_odd(int(input("Enter num: "))))
