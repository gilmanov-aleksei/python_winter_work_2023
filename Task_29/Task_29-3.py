#! /usr/bin/python

# Задача 29-3

# Напишите функцию, которая проверяет, являются ли два слова изоморфными.
# Два слова изоморфны, если буквами одного слова можно сопоставить (map)
# буквами другого слова.

# True:
# CBAABC DEFFED
# XXX c
# RAMBUNCTIOUSLY THERMODYNAMICS

# False:
# AB CC
# XXY XYY
# ABAB CD

def isomorphic_words(s1, s2):
    return s1 + "-" + s2


str1 = ["CBAABC", "XXX", "RAMBUNCTIOUSLY", "AB", "XXY", "ABAB"]
str2 = ["DEFFED", "ABAB", "THERMODYNAMICS", "CC", "XYY", "CD"]

for i in range(len(str1)):
    print(isomorphic_words(str1[i], str2[i]))
