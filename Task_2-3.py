#! /usr/bin/python

# Вводим число
n = int(input("Введите число: "))
# Начальное значение переменой "f"
f = 1
for i in range(2,n+1):
    # Вычисляем факториала числа "n"
    f = f * i
# Выводим на экран результат вычисления
print("Факториал числа",n,"равен:",f)