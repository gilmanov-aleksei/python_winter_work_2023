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
    # Словарь для сопоставления символов строки s1 со строкой s2.
    d = {}
    # Множество для сопоставленных символов.
    s = set()
    for i in range(len(s1)):
        x = s1[i]
        y = s2[i]
        if x in d:
            if d[x] != y:
                return False
        else:
            if y in s:
                return False

            d[x] = y
            s.add(y)

    return True


str1 = ["CBAABC", "XXX", "RAMBUNCTIOUSLY", "AB", "XXY", "ABAB"]
str2 = ["DEFFED", "ABAB", "THERMODYNAMICS", "CC", "XYY", "CD"]

for i in range(len(str1)):
    print(isomorphic_words(str1[i], str2[i]))
