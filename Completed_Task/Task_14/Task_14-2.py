#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет сумму цифр натурального числа

def num_sum(n):
    # Базовый случай, если ноль,
    if n == 0:
        # то возвращаяем 0
        return 0
    return n % 10 + num_sum(n // 10)


print(f"Sum of numbers:", num_sum(abs(int(input("Enter the number: ")))))
