#! /usr/bin/python

x = "224438789387682902209379098706"
print(x)
#x = int(input(Введите число и нажмите Enter: "))

# Разделяем цифры в строке, между ними записываем пробелы
y1 = (''.join(map(lambda z: z + ' ', x)))
# Создаём список из строки цифр
y = list(map(int, y1.split()))
# Сортируем список цифр по возрастанию
s = sorted(y)
# Печатаем количество цифр в списке
print("Цифр в строке:", len(y))
print(f"Ч - Кол.")
for i in range(0, 10):
    # Печатаем число - печатаем количество этого числа найденого в списке
    print(i, "-", s.count(i))
