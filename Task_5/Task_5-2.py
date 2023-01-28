#! /usr/bin/python

n = int(input("Введите число: "))
d = {}
k = 1
for i in range(1, int(n / 2) + 1):
    if n % i == 0:
        d.setdefault(k, i)
        k += 1
d.setdefault(k, n)
print(f"Для числа {str(n)} все его делители: ", end=' ')
for k, v in d.items():
    print(v, end=' ')
