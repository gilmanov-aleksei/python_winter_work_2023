#! /usr/bin/python

n = int(input("Введите число: "))
n = int(n) - 2
f1 = f2 = 1
print("Значения элемента:", f1, f2, end=' ')
while n > 0:
    f1, f2 = f2, f1 + f2
    n -= 1
    print(f2, end=' ')


