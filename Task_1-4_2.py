#! /usr/bin/python
import random

# Генерация случайных чисел для X и Y
x = random.randint(-9,9)
y = random.randint(-9,9)

# Вводим первое число
#x = int(input("Введите число X: "))
# Вводим второе число
#y = int(input("Введите число Y: "))

# Проверка второго числа на 0
if y == 0:
    print("Делить на 0 нельзя!")
    quit()
else:
# Вычисляем значение
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x // y
    f = x ** y

# Выводим на экран значение X и Y
print("X =",x, "Y =",y)

# Сравниваем X и Y между собой, результат выводим на экран
if x < y:
    print('X меньше Y')
elif x == y:
    print('X равен Y')
else:
    print('X больше Y')

# Выводим результат примеров на экран
print("X+Y =",a,"  X-Y =",b,"  X*Y =",c,"  X/Y =",d,"  X//Y =",e,"  X**Y =",f)

# Обнуляем счётчики
k = l = m = n = o = p = 0

# Сравниваем полученый результат

if a > b:
    k = k + 1
else:
    l = l + 1
if a > c:
    k = k + 1
else:
    m = m + 1
if a > d:
    k = k + 1
else:
    n = n + 1
if a > e:
    k = k + 1
else:
    o = o + 1
if a > f:
    k = k + 1
else:
    p = p + 1

# --------
if b > c:
    l = l + 1
else:
    m = m + 1
if b > d:
    l = l + 1
else:
    n = n + 1
if b > e:
    l = l + 1
else:
    o = o + 1
if b > f:
    l = l + 1
else:
    p = p + 1

# --------
if c > d:
    m = m + 1
else:
    n = n + 1
if c > e:
    m = m + 1
else:
    o = o + 1
if c > f:
    m = m + 1
else:
    p = p + 1

# --------
if d > e:
    n = n + 1
else:
    o = o + 1
if d > f:
    n = n + 1
else:
    p = p + 1

# --------
if e > f:
    o = o + 1
else:
    p = p + 1

# Определяем первое наибольшое число
if k == 5:
    print(f"Первое наибольшее число: ",a)
if l == 5:
    print(f"Первое наибольшее число: ",b)
if m == 5:
    print(f"Первое наибольшее число: ",c)
if n == 5:
    print(f"Первое наибольшее число: ",d)
if o == 5:
    print(f"Первое наибольшее число: ",e)
if p == 5:
    print(f"Первое наибольшее число: ",f)

# Определяем второе наибольшое число
if k == 4:
    print(f"Второе наибольшее число: ",a)
if l == 4:
    print(f"Второе наибольшее число: ",b)
if m == 4:
    print(f"Второе наибольшее число: ",c)
if n == 4:
    print(f"Второе наибольшее число: ",d)
if o == 4:
    print(f"Второе наибольшее число: ",e)
if p == 4:
    print(f"Второе наибольшее число: ",f)
