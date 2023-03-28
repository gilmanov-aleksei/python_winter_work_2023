#! /usr/bin/python

# Задача 28-2 Напишите функцию, результатом которой является расстояние
# Хемминга двух строк одинаковой длины, равное по количеству
# несовпадающих букв на одинковых позициях.
# Например:
# abc и abc - 0
# abc и abd - 1
# abc и xyz - 3

def find_simbol(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


srt1 = "abc"
srt2 = "abc"
print(f"{srt1} и {srt2} - {find_simbol(srt1, srt2)}")
srt1 = "abc"
srt2 = "abd"
print(f"{srt1} и {srt2} - {find_simbol(srt1, srt2)}")
srt1 = "abc"
srt2 = "xyz"
print(f"{srt1} и {srt2} - {find_simbol(srt1, srt2)}")
