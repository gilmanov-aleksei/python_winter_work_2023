#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет количество
# цифры введенного натурального числа

def num_len(n):
    n //= 10
    if n == 0:
        return 1
    return 1 + num_len(n)


print(num_len(abs(int(input("Enter the number: ")))))
