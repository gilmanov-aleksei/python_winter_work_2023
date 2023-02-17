#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def summ_num(n):
    if n == 0: return 0
    return n % 10 + summ_num(n // 10)


print(summ_num(int(input("Enter num: "))))
