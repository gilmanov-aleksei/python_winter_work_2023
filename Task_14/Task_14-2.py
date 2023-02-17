#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def summ_nat(n):
    if n == 0: return 0
    return n % 10 + summ_nat(n // 10)


print(summ_nat(int(input("Enter num: "))))



