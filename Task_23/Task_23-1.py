#! /usr/bin/python

# Найдите длину наибольшей подстроки данной строки, которая
# является палиндромом.
# Например, дана строка 'aabbccddcc' тогда длиной подстроки с
# наибольшим палиндромом является 6 (подстрока 'ccddcc')

def find_long_palindrome(txt):
    # Создаём пустой словарь для сбора полиндромов
    dct = {}
    # Переменная максимальной длины полиндорма
    max_len = 2
    # Цикл перебора всей строки
    for i in range(len(txt)):
        # Цикл перебора по элементно
        for j in range(len(txt), i, -1):
            # Срез строки в переменную x
            x = txt[i:j]
            # Длину среза строки в переменную lx
            lx = len(x)
            # Сравниваем срез строки с его перевернутым срезом,
            # то пропускаем, так как не полиндром
            # И длину полиндрома, если он меньше предыдущего , то пропускаем
            if x == x[::-1] and lx >= max_len:
                # Записывем длину палендрома
                max_len = lx
                # Если они равны, проверить ключ в словаре, если он есть,
                # добавляем в значение к текущему списку, новый полиндром
                if lx in dct:
                    dct[lx].append(x)
                # Если нет, то в значение создаем список с полиндромом
                else:
                    dct[lx] = [x]
    # Находим максимальную число в ключе словаря, это длина полиндрома
    # max_len = max(dct.keys())
    # Максимальное значения ключа сохраняем в список
    word = dct.get(max_len)
    # Преобразуем список в строку
    word = ', '.join(word)
    return word, max_len


string = 'aababcacdedcaceeefffeeeklmonmlka1s2d3d2s1ceeefffeeek'
flp = find_long_palindrome(string)
# Результат выводим на экран
print("Палиндром:", flp[0])
print("Длина полиндрома:", flp[1])
