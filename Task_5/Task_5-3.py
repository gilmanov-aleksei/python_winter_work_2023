#! /usr/bin/python

n = int(input("Введите число: "))
f1 = 0
f2 = 1
fs = 0
i = 0
print("Значение этого элемента:", f1, f2, end=' ')
while i < n - 1:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    i += 1
    print(f2, end=' ')
