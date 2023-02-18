#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет количество
# цифры введенного натурального числа

def num_count(n):
    n //= 10
    if not n:
        return 1
    return 1 + num_count(n)


print(num_count(abs(int(input("Enter num: ")))))
