#! /usr/bin/python

# Задача 19-1
# В кошельке лежат бумажные купюры 50, 100, 200, 500, 1000, 5000 рублей,
# каждой купюры по одной штуке.
# Какие суммы можно составить, если использовать по три купюры из них?

# while True:
#     n = input("Введите 3 и более числа через пробел и нажите Enter, 0 - выход: ").split()
#     if '0' in n:
#         break
#     if len(n) < 3:
#         print("Введено меньше 3 чисел, повторите ввод.")
#     else:
#         n = list(map(int, n))
#         s = []
#         for i in range(len(n)):
#             for j in range(i + 1, len(n)):
#                 for k in range(j + 1, len(n)):
#                     s.append(n[i] + n[j] + n[k])
#         print("Суммы трех чисел из списка:", s)

n = [50, 100, 200, 500, 1000, 5000]
s = []
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        for k in range(j + 1, len(n)):
            s.append(n[i] + n[j] + n[k])
print(*n)
print(*s)
