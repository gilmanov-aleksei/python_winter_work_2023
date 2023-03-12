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

word = input("Input word: ")
# Список для гласных букв
vowels = []
# Список для согласных букв
consonants = []
# Перебор слова по буквам
for letter in word:
    # Сравниваем букву со списком гласных букв
    if letter in "aeiouy":
        # если гласная, сохраняем в список гласных
        vowels.append(letter)
    else:
        # согласную сохраняем в список для согласных
        consonants.append(letter)
    # Проверяем длину спискоков гласных и согласных букв
# Создаем пустую строку для перемешивания букв
result = ""
if abs(len(vowels) - len(consonants)) > 1:
    # Если больше 1, то выводин на экран Impossible!
    print("Impossible!")
else:
    # Цикл повторять пока не списки не станут пустыми
    while vowels or consonants:
        # Прверяем длину скисков
        if len(vowels) < len(consonants):
            # Если согласных больше чем гласных,
            # то записываем в строку согласную
            result += consonants.pop(0)
        else:
            # иначе записываем в строку гласную
            result += vowels.pop(0)
    # Выходим с новой строкой

print(result)
