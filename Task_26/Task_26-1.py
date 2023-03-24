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
    # если строки равны
    if str1 == str2:
        return True
    # если длины строк различаются более чем на 1 символ
    if abs(len(str1) - len(str2)) > 1:
        return False
    # счетчик для подсчета различающихся символов
    count_diff = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            count_diff += 1
            if count_diff > 1:
                return False

    return True


print(compare_str('abc', 'abc'))  # True
print(compare_str('abc', 'abcd'))  # True
print(compare_str('bc', 'abc'))  # True
print(compare_str('axc', 'abc'))  # True
print(compare_str('abc', 'acb'))  # False
print(compare_str('abc', 'a'))  # False
print(compare_str('', '   '))  # False
