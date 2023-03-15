#! /usr/bin/python

# Найдите длину наибольшей подстроки данной строки, которая
# является палиндромом.
# Например, дана строка 'aabbccddcc' тогда длиной подстроки с
# наибольшим палиндромом является 6 (подстрока 'ccddcc')

def find_long_palindrome(txt):
    max_len = 0
    word = ''
    dct = {}
    for i in range(len(txt)):
        for j in range(len(txt), i, -1):
            x = txt[i:j]
            if x == x[::-1]:
                if max_len <= len(x):
                    max_len = len(x)
                    dct[x] = dct.get(x, len(x))
    for key, value in dct.items():
        if value == max_len:
            word += key + ' '
    return word, max_len


string = 'aababcacdedcaceeefffeeeklmonmlka1s2d3d2s1'
flp = find_long_palindrome(string)

print("Палиндромы:", flp[0])
print("Длина полиндрома:", flp[1])

# Рабочий вариант
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
