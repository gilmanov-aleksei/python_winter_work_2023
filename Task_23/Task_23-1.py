#! /usr/bin/python

# Найдите длину наибольшей подстроки данной строки, которая
# является палиндромом.
# Например, дана строка 'aabbccddcc' тогда длиной подстроки с
# наибольшим палиндромом является 6 (подстрока 'ccddcc')

def find_long_palindrome(txt):
    # Создаём пустой словарь для сбора полиндромов
    dct = {}
    # Цикл перебора всей строки
    for i in range(len(txt)):
        # Цикл перебора по элементно
        for j in range(len(txt), i, -1):
            # Сравниваем срез строки и его перевернутым срез
            if txt[i:j] == txt[i:j][::-1]:
                # Если они равны, записываем строку в ключ,
                # в значение его длину
                dct[txt[i:j]] = dct.get(txt[i:j], len(txt[i:j]))
    # Находим максимальную длину в значение словаря
    max_len = max(dct.values())
    # перебераем все ключи словаря,
    # с проверкой максимального значения и сохраняем в список
    keys = [k for k, v in dct.items() if v == max_len]
    # Преобразуем список в строку
    word = ', '.join(keys)
    return word, max_len


string = 'aababcacdedcaceeefffeeeklmonmlka1s2d3d2s1'
flp = find_long_palindrome(string)
# Результат выводим на экран
print("Палиндром:", flp[0])
print("Длина полиндрома:", flp[1])

# Рабочий вариант со списком
# def find_long_palindrome(txt):
#     max_len = 0
#     word = []
#     for i in range(len(txt)):
#         for j in range(len(txt), i, -1):
#             x = txt[i:j]
#             if x == x[::-1]:
#                 if max_len <= len(x):
#                     max_len = len(x)
#                     word.append(x)
#     word = word[::-1]
#     for w in word:
#         if len(w) > len(w[-1]):
#             word.pop()
#     return word, max_len
