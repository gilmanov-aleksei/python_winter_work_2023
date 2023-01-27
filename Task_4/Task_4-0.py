#! /usr/bin/python

s = input('Введите два слова через пробел: ').split()
# Записываем слова в список
word1 = list(s[0])
word2 = list(s[1])
# Переменная chek: 1 - True, 0 - False
chek = 1
# Индекс
i = 0
# Сравниваем длину слов
if len(s[0]) != len(s[1]):
    # Если не равны, то chek=0 и выход
    chek = 0
else:
    # Если равны, сортируем каждое слово
    word1.sort()
    word2.sort()
    # Цикл на всю длину слова
    while i < len(s[0]):
        # Сравниваем каждый элемент в двух слова
        if word1[i] != word2[i]:
            # Если не равны, то chek=0 и выход
            chek = 0
            break
        else:
            # Прибавляем индекс
            i += 1
# Прверяем chek: 1 - True, 0 - False
if chek == 1:
    print(True)
else:
    print(False)
