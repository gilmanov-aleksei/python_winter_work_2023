#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def summ(n):
    if n == 0: return 0
    return n % 10 + summ(n // 10)


print(summ(int(input("Enter num: "))))



