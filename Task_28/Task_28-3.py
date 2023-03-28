#! /usr/bin/python

# Задача 28-3

# Напишите функцию, которая рассчитывает наименьшее число перестановок при перемещении
# Ханойской башни ( n дисков насаженных на одном стержне). Требуется переместить эти диски на
# соседний стержень. Разрешается использовать третий стержень. Диски можно класть только на диски
# большего диаметра.
# Для n = 1 , число перестановок равно 1
# Для n = 2 , число перестановок равно 3

def hanoi_tower(n):
    return 1 + 2 * hanoi_tower(n - 1) if n != 1 else 1
    # return 1 if n == 1 else 1 + 2 * hanoi_tower(n - 1)
    # базовый случай
    # if n == 1:
    #     return 1
    # else:
    #     return 1 + 2 * hanoi_tower(n - 1)


print("Ханойская башня")
while True:
    num = int(input("Введите число дисков, 0 - Выход: "))
    if num != 0:
        print(f"Число перестановок равно: {hanoi_tower(num)}")
    else:
        break
