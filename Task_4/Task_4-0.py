#! /usr/bin/python

s = input().split()

word1 = list(s[0])
word2 = list(s[1])
lens1 = len(s[0])

if lens1 != len(s[1]):
    chek = False
else:
    word1.sort()
    word2.sort()
    chek = True
    i = 0
    while i < lens1:
        if word1[i] == word2[i]:
            i += 1
        else:
            chek = False
print(chek)
