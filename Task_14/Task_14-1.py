#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет количество
# цифры введенного натурального числа

def num_len(n):
    # Делим число на 10 без остатка
    n //= 10
    # Базовый случай, если ноль,
    if n == 0:
        # то возвращаяем 1
        return 1
    # иначе, прибавляем на 1
    return 1 + num_len(n)


print(f"Number length:", num_len(abs(int(input("Enter the number: ")))))
