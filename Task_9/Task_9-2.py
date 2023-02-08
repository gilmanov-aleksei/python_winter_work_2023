#! /usr/bin/python

# Задача 9-2
# Напишите программу, которая определяет и печатает «похожие» слова.
# Слово называется похожим на другое слово, если его гласные буквы
# находятся там же, где находятся гласные буквы другого слова, например:
# дорога и пароход похожие слова гласные буквы на втором, четвертом и
# шестом местах), станок и прыжок - похожие слова , питон и удав непохожие слова.
# Считаем, что в русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е).
# Ввод:
# x - первое слово, например, питон.
# n - количество слов для сравнения, например 6.
# Дальше вводятся 6 слов, например: поросенок, титан, итог, лавка, погост, кино.
# Вывод - слова, похожие на питон:
# титан, погост, кино

# str1 = input("Введите первое слов: ")
# str2 = input("Введите слова через пробел: ")
s1 = 'питон'
s2 = 'титан итог лавка погост кино' # поросенок
glas = {'а': 0, 'у': 0, 'о': 0, 'ы': 0, 'и': 0, 'э': 0, 'я': 0, 'ю': 0, 'ё': 0, 'е': 0, }
gls1 = 0
sl1 = list(s1)
for i, j in enumerate(sl1):
    if j in glas:
        gls1 += 1
print('Слова, похожие на:', s1)
sl2 = s2.split()
lsl2 = len(sl2)
for i in sl2:
    sl3 = list(i)
    lsl3 = len(i)
    gls2 = 0
#    print(i)
    if lsl2 <= lsl3 + 2 or lsl2 == lsl3:
        for c, v in enumerate(sl1):
            if v in glas:
                if c < lsl3 and sl3[c] in glas:
                    gls2 += 1
        if gls1 == gls2:
            print(''.join(map(str, sl3)))

# 0 <= sl3[c] < len(sl3) and