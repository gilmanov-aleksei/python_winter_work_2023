#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def num_sum(n):
    if n == 0:
        return 0
    return n % 10 + num_sum(n // 10)


print(num_sum(abs(int(input("Enter the number 1: ")))))


# ---------------------------------------

def sum_dig(m):
    return m % 10 + sum_dig(m // 10) if m > 9 else m


print(sum_dig(abs(int(input("Enter the number 2: ")))))
