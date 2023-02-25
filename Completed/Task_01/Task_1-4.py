#! /usr/bin/python
# Вводим первое число
x = int(input("Введите число X: "))
# Вводим второе число
y = int(input("Введите число Y: "))

# Проверка второго числа на 0
if y == 0:
    print("Делить на 0 нельзя!")
    input()
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

# Сравниваем полученый результат
val1 = (a, b, c, d, e, f)

max1 = val1[0]
for i in val1:
    if i > max1:
        max1 = i

print(f"Наибольшее число: {max1}")