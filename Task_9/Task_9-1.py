#! /usr/bin/python

# Функция замены ДНК на РНК
def dna_to_rnk(dna):
    # Пустая строка для РНК
    rnk = ""
    # Цикл по всем символам ДНК
    for k in dna:
        # По ключю в словаре ДНК находим значение
        # и записываем его в конец строки РНК
        rnk += ddna.get(k)
    # Выход из функции
    return rnk


# Словарь ДНК
ddna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'T'
}

# Ввод строки с переводм в верхний регистр
sdnk = str(input("Enter DNA letters: ")).upper()
# Читаем все ключи из словаря
keys = ddna.keys()
# Цикл проверки вводимых букв,
for i in sdnk:
    # если буква не соотвествует ключу словаря,
    # то она пропускается, так же цифры и символы
    if i in keys:
        # если совподает, то записываем её в строку ДНК.
        dnk += ddna.get(i)
# Пустая cтрока для сбора правильнывх букв ДНК
dnk = ""
# Прверка вводимой строки,
if len(dnk) != 0:
    # если есть буквы ДНК, то
    # Выводим на экран строку ДНК
    print(dnk)
    # Выводим на экран строку из черточек
    # по длине строки ДНК
    print("-" * len(dnk))
    # Выводим на экран значения РНК,
    # полученные через функцию замены ДНК на РНК
    print(dna_to_rnk(dnk))
else:
    print("No DNA letters!")
    input("Press Enter to exit.")
