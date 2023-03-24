#! /usr/bin/python

# Задача 26-1

# Напишите функцию, которая сравнивает две строки и выдает True,
# если между ними есть не более, чем 1 разница в буквах, и False во
# всех остальных случаях. Если две строки равны, то True.
# Например:
# 'abc' и 'abc' - True, 'abc' и abcd ' - True,
# 'bc' и 'abc' - True, 'axc' и 'abc' - True
# 'abc' и 'acb' - False, 'abc' и 'a' - False, '' и '   ' - False

def compare_str(str1, str2):
    # Если строки равны, то True
    if str1 == str2:
        return True
    # Если строк различаются более чем на 1 символ, то False
    if abs(len(str1) - len(str2)) > 1:
        return False
    # Меняем местами строки, если str2 больше str1
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    for i in range(len(str2)):
        if str1[i] != str2[i]:
            if len(str1) == len(str2):
                return str1[i + 1:] == str2[i + 1:]
            else:
                return str1[i + 1:] == str2[i:]

    return True


print(compare_str('abc', 'abc'))  # True
print(compare_str('abc', 'abcd'))  # True
print(compare_str('bc', 'abc'))  # True
print(compare_str('axc', 'abc'))  # True
print(compare_str('abc', 'acb'))  # False
print(compare_str('abc', 'a'))  # False
print(compare_str(' ', '   '))  # False
