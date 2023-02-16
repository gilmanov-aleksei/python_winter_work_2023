#! /usr/bin/python

# программа начата и не закончена

# Задание
# Введено слово (латинские буквы в нижнем регистре).
# Перетасуйте его буквы, чтобы гласные и согласные шли по очереди.
# Если это невозможно, то выдайте "Impossible!"
# Гласными будем считать только
# a, e, i , o, u. Остальные согласные.
# Например:
# apple -> papel
# idea -> Impossible!
# sorted --> Impossible!
# idiot -> idito
def sort_word(k,v):
    pass
    return

s = input("Enter a word: ")
d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
glas = []
soglas = []

# Разделение слова в список букв
let = [y for w in s for y in w]
# проверка каждой буквы со словарем гласных,
# если есть, записывается его индекс в список
# функция возвращает список индексов гласных в слове
# lst = [i for i, j in enumerate(let) if j in d]
for i, j in enumerate(let):
    if j in d:
        glas.append(i)
    else:
        soglas.append(i)
print(glas)
print(soglas)
if len(glas) == len(soglas):
    print("Rovno")
elif len(glas) - 1 == len(soglas):
    print("Bolshe")
elif len(glas) + 1 == len(soglas):
    print("Menshe")
else:
    print("Impossible!")
