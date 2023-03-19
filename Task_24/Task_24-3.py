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
    i = 0
    for char in string:
        if char == '(':
            i += 1
        elif char == ')':
            if not i:
                return i == 1
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

