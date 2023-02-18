#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def num_sum(n):
    # Базовый случай, если ноль,
    if n == 0:
        # то возвращаяем 0
        return 0
    # иначе, получаем остаток от деления на 10,
    # число делем на 10 без остатка
    return n % 10 + num_sum(n // 10)

def sum_dig(m):
    return m % 10 + sum_dig(m // 10) if m > 9 else m


print(f"Sum of numbers:", num_sum(abs(int(input("Enter the number 1: ")))))
print()
print(f"Sum of numbers:", sum_dig(abs(int(input("Enter the number 2: ")))))
