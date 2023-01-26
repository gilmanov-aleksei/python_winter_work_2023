#! /usr/bin/python

s = input('Введите два слова через пробел: ').split()

word1 = list(s[0])
word2 = list(s[1])
chek = True
i = 0

if len(s[0]) != len(s[1]):
    chek = False
else:
    word1.sort()
    word2.sort()
    while i < len(s[0]):
        if word1[i] == word2[i]:
            i += 1
        else:
            chek = False
print(chek)
