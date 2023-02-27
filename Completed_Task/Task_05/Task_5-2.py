#! /usr/bin/python

# Задача 5-2
# 1. Ввести число. Напечатать все его делители.
# Например: 12
# Вывод: 1 2 3 4 6 12
# 2. Более сложный вариант, напечатать только его простые делители и их степени.
# Например: 12 (12 = (2 ** 2) * (3 ** 1))
# Вывод:
# 2-2
# 3-1

n = int(input("Введите число: "))
# Пустой словарь
d = {}
# Начальный ключ для словаря
k = 1

# Цикл от 1 до n числа деленного на 2,
# так как, всё что больше, будет с остатком.
for i in range(1, int(n / 2) + 1):
    # Прверяем остаток от деления
    if n % i == 0:
        # Если остатка нет, то записываем
        # значение i в словарь
        d.setdefault(k, i)
        # Изменяем значение, для нового ключа
        k += 1

# Записываем значение n в последний ключ,
# так как число n может быть собственным делителем
d.setdefault(k, n)

print(f"Для числа {str(n)}, все его делители: ", end=' ')
# В цикле выводим все значения ключей из словаря
for k, v in d.items():
    print(v, end=' ')