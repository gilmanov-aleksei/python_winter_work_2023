#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def summ_num(n):
    if n == 0:
        return 0
    return n % 10 + summ_num(n // 10)


print(summ_num(abs(int(input("Enter num1: ")))))


# ---------------------------------------

def sum_dig(m):
    return m % 10 + sum_dig(m // 10) if m > 9 else m


print(sum_dig(abs(int(input("Enter num2: ")))))
