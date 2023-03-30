#! /usr/bin/python

# Задача 29-3

# Напишите функцию, которая проверяет, являются ли два слова изоморфными.
# Два слова изоморфны, если буквами одного слова можно сопоставить (map)
# буквами другого слова.
#
# True:
# CBAABC DEFFED
# XXX YYY
# RAMBUNCTIOUSLY THERMODYNAMICS
#
# False:
# AB CC
# XXY XYY
# ABAB CD

def isomorphic_words(s1, s2):
    # Если s1 и s2 имеют разную длину, они не могут быть изоморфны
    if len(s1) != len(s2):
        return False
    # Словарь для хранения сопоставления строки s1 со строкой s2.
    dct = {}
    # Множество для хранения уже сопоставленных символов.
    sets = set()
    for i in range(len(s1)):
        # Если s1[i] уже был раньше
        if s1[i] in dct:
            # возвращает False, если вхождение s1[i] находиться в s2[i]
            if dct[s1[i]] != s2[i]:
                return False
        # , если x виден в впервые
        else:
            # возвращает False, если s2[i] уже сопоставлен с каким-либо символом в s1
            if s2[i] in sets:
                return False
            # Cопоставляет s1 с s2 и помечаем как сопоставленный
            dct[s1[i]] = s2[i]
            sets.add(s2[i])
    return True


str1 = ["CBAABC", "XXX", "RAMBUNCTIOUSLY", "AB", "XXY", "ABAB"]
str2 = ["DEFFED", "YYY", "THERMODYNAMICS", "CC", "XYY", "CD"]

for i in range(len(str1)):
    print(str1[i], str2[i], "--->", isomorphic_words(str1[i], str2[i]))
