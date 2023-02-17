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
s = "appely"
d = 'aeiouy'

# Разделение слова в список букв
si = [y for w in s for y in w]

glas = [x for x in (si) if x in d]
soglas = [y for y in (si) if not y in d]

lg = len(glas)
ls = len(soglas)

# sum(2 for letter in s if letter in vowels) > len(s)
if lg == ls or lg + 1 == ls:
    glas.append(' ')
    glas.sort()
    print(sort_word(lg))
elif lg - 1 == ls:
    soglas.append(' ')
    print(sort_word(lg))
else:
    print("Impossible!")

print(glas)
print(soglas)
