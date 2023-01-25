#! /usr/bin/python

l = "aaa bbb aaa ccc ddd bbb aaa"
lst = l.split()
counter = {}
max=word = ''
max_cou = 0
for word in lst:
    if word not in counter:
        counter[word] = 0
    counter[word] += 1
    if counter[word] > max_cou:
        max_cou = counter[word]
        max_word = word
print(f"Слово = {max_word}   Сколько = {max_cou}")


