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

# # Разделение слова в список букв
# let = [l for w in word for l in w]
# # проверка каждой буквы со словарем гласных,
# # если есть, записывается его индекс в список
# # функция возвращает список индексов гласных в слове
# return [i for i, j in enumerate(let) if j in glas]

s = input("Enter a word: ")
d = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}

s1 = sorted(list(s))
gl = 0
sg = 0
print(s1)
for i in range(len(s1) + 1):
    if gl > sg + 2 or gl:
        if gl + 1 == sg:
            pass
        elif gl - 1 == sg:
            pass
