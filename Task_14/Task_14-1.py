#! /usr/bin/python

# Напишите рекурсивную функцияю,
# которая вычисляет количество
# цифры введенного натурального числа
def col_num(n):
    if n == 0: return 0
    return n + col_num(n % 10)

print(col_num(int(input("Enter num: "))))

