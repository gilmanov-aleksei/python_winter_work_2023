#! /usr/bin/python

# Задача 25-3

# Напишите функцию, которой на вход подается строка, содержащая
# последовательность слов (которые могут включать буквы верхнего и нижнего
# регистра). На выходе должна получиться строка в CamelStyle
# Например, "camel case word" => CamelCaseWord

# Вариант 1
def camel_style(string):
    # Пустая строка для сбора слов
    new_str = ""
    # Все слова начинаются с заглавной буквы
    # и продолжаются строчными, методом title()
    # Методом split() переводит строку в список, через разделитель
    words = string.title().split(" ")
    # Цикл по списку
    for word in words:
        # Каждое слово прибавляем в новую строку
        new_str += word
    return new_str


print("Вариант 1")

text1 = "caMel cASe wORd"
print(camel_style(text1))

print("Вариант 2")


# Вариант 2
def to_camel_style(string):
    # используем генератор списков для создания списка, с помощью метода capitalize(),
    # переводя первую буквы в верхний регистр, а остальные в нижний.
    # и затем объединяем их с помощью метода join()
    return ''.join(word.capitalize() for word in string.split())


text2 = "caMel cASe wORd"
print(to_camel_style(text2))
