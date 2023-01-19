#! /usr/bin/python

# Вводим первое число
x = int(input("Введите число X: "))
# Вводим второе число
y = int(input("Введите число Y: "))

# Вычисляем значение
a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
f = x ** y

# Выводим на экран значение X и Y
print("X =",x,"Y =",y)

# Сравниваем X и Y между собой, результат выводим на экран
if x < y:
    print('X меньше Y')
elif x == y:
    print('X равен Y')
else:
    print('X больше Y')

# Выводим результат примеров на экран
print("X+Y =",a,"  X-Y =",b,"  X*Y =",c,"  X/Y =",d,"  X//Y =",e,"  X**Y =",f)

# Сравнение результатов, код найден в интернете, применён для выполнения теукщей задачи

# Сравниваем полученый результат через MAX
l_num1 = (a, b, c, d, e, f)
max_num = max(l_num1)
print("Первое наибольшее число через MAX:", max_num)

# Сравниваем полученый результат через FOR
def calc_largest(arr):
    second_largest = arr[0]
    largest_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest_val:
            largest_val = arr[i]

    for i in range(len(arr)):
        if arr[i] > second_largest and arr[i] != largest_val:
            second_largest = arr[i]

    return second_largest

z = calc_largest([a, b, c, d, e, f])
print("Второе наибольшее число через FOR:",z)

# Сравниваем полученый результат через SORT
values = [a, b, c, d, e, f]
values.sort()
print(f"Третье наибольшее число через SORT: {values[-3]}")