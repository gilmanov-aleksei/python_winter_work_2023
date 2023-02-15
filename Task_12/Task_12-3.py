#! /usr/bin/python

# Задача 12-3
# Напишите функцию, которая на вход принимает
# строку диапазонов натуральных чисел,
# например: '1-2, 4-4, 3-6'
# На выходе функция должна сформировать список натуральных чисел,
# которые попадают в один из этих диапазонов,
# например: [1,2,4,3,4,5,6]

def str_to_lst(string):
    return [j for i in string.split(', ') for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1)]

    # strlst = []
    # for i in s.split(', '):
    #     k = i.split('-')
    #     for j in range(int(k[0]), int(k[1]) + 1):
    #         strlst.append(j)


# s = input("Введите диапозон натуральных чисел: ").replace(" ", ", ")
s = '1-2, 4-4, 3-6, 10-20'
print(s)
print(str_to_lst(s))
