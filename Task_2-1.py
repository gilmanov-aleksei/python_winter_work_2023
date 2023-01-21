#! /usr/bin/python

# Вводим число
n = int(input("Введите число: "))
print("Таблица умножения на",n,"от 1 до 9")
# Цикл от 1 до 10 с шагом 1
for i in range(1, 10):
    print(i,"x",n,"=",i*n)
