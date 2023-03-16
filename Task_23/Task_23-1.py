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
            # Если длина меньше 2, то пропукаем, так как не полиндром
            # Сравниваем срез строки и его перевернутым срез
            if txt[i:j] == txt[i:j][::-1] and len(txt[i:j]) > 1:
                # Если они равны, записываем длину в ключ,
                # а в значение строку
                if dct.get(len(txt[i:j]), True) != True:
                    lst = dct[len(txt[i:j])]
                    lst.append(txt[i:j])
                    dct[len(txt[i:j])] = lst
                else:
                    dct[len(txt[i:j])] = txt[i:j].split()

    # Находим максимальную длину в ключе словаря
    max_len = max(dct.keys())
    # проверка максимального значения ключа и сохраняем в список
    word = dct.get(max_len)
    # Преобразуем список в строку
    word = ', '.join(word)
    return word, max_len


string = 'aababcacdedcaceeefffeeeklmonmlka1s2d3d2s1ceeefffeeek'
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
