#! /usr/bin/python

# Задача 24-3
#
# Создайте функцию, которая принимает на входе строку из круглых скобок,
# открывающих и закрывающих, и возвращает True или False , если строка
# является «правильной», т.е. никогда количество закрывающих не больше,
# чем количество открывающих, если двигаться по строке слева направо.
# Примеры:
# "()" => true
# ")(()))" => false
# "(" => false
# "(()) (( ()() ) () )" => true

def string_validation(string):
    # Переменная для подсчёта скобок
    i = 0
    # Цикл по строке
    for char in string:
        # Проверяем символ из строки,
        # если окрывающая скобка,
        if char == '(':
            # то прибавлем переменную на 1
            i += 1
        # если закрывающая стрка, то убавляем на 1
        elif char == ')':
            #
            if not i:
                return False
            else:
                i -= 1
    return i == 0


str = "()"  # => true
print(string_validation(str))
str = ")(()))"  # => false
print(string_validation(str))
str = "("  # => false
print(string_validation(str))
str = "(()) (( ()() ) () )"  # => true
print(string_validation(str))
str = ")("  # => true
print(string_validation(str))

