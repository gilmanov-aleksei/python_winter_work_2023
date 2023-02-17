#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def summ_num(n):
    if n == 0:
        return 0
    return n % 10 + summ_num(n // 10)


print(summ_num(int(input("Enter num: "))))


def sum_digits(m):
    return m % 10 + sum_digits(m // 10) if m > 9 else m


print(sum_digits(int(input("Enter num: "))))
