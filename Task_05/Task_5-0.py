#! /usr/bin/python

# программа начата и не закончена

# Задание
# Введено слово (латинские буквы в нижнем регистре).
# Перетасуйте его буквы, чтобы гласные и согласные шли по очереди.
# Если это невозможно, то выдайте "Impossible!"
# Гласными будем считать только
# a, e, i, o, u, y. Остальные согласные.
# Например:
# apple -> papel
# idea -> Impossible!
# sorted --> Impossible!
# idiot -> idito
def sort_word(v):
    srt = ""
    for i in range(v):
        srt += glas[i]
        srt += soglas[i]
    return srt


# s = input("Enter a word: ")
s = "appaale"
d = 'aeiouy'

# Разделение слова в список букв
# si = [y for w in s for y in w]

glas = [x for x in s if x in d]
soglas = [y for y in s if not y in d]

lg = len(glas)
ls = len(soglas)
print(glas)
print(soglas)

# sum(2 for letter in s if letter in vowels) > len(s)
if lg == ls:
    print(s, "-->", sort_word(lg))
elif lg + 1 == ls:
    glas.append(" ")
    print(s, "-->", sort_word(ls))
elif lg - 1 == ls:
    soglas.append(" ")
    print(s, "-->", sort_word(lg))
else:
    print(s, "--> Impossible!")
