#! /usr/bin/python

x = "404388945311416890550939019806"
# x = input("Введите число и нажмите Enter: ")
print(x)
# Создаём пустой список
y = []
for i in range(0, len(x), 1):
    # Записываем в новый список все цифры из строки
    y.append(int(x[i: i + 1]))
# Сортируем список цифр по возрастанию
s = sorted(y)
# Печатаем количество цифр в списке
print("Цифр в строке:", len(y))
print(f"Ч - Кол.")
for j in range(0, 10):
    # Печатаем число - печатаем количество этого числа найденого в списке
    print(j, "-", s.count(j))