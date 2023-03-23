#! /usr/bin/python

# Задача 26-1

# Напишите функцию, которая сравнивает две строки и выдает True,
# если между ними есть не более, чем 1 разница в буквах, и False во
# всех остальных случаях. Если две строки равны, то True.
# Например:
# 'abc' и 'abc' - True, 'abc' и abcd ' - True,
# 'bc' и 'abc' - True, 'axc' и 'abc' - True
# 'abc' и 'acb' - False, 'abc' и 'a' - False, '' и '   ' - False

def compare_strings(s1, s2):
    # если строки равны
    if s1 == s2:
        return True

    # если длины строк различаются более чем на 1 символ
    if abs(len(s1) - len(s2)) > 1:
        return False
    # счетчик для подсчета различающихся символов
    count_diff = 0

    # проходимся по символам двух строк и считаем число различающихся символов
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            count_diff += 1
            if count_diff > 1:
                return False
            if len(s1) > len(s2):
                i += 1
            elif len(s1) < len(s2):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    # учитываем случай, когда различающийся символ - последний
    if i < len(s1) or j < len(s2):
        count_diff += 1
    # возвращаем True, если различается не более 1 символа
    return count_diff == 1


print(compare_strings('abc', 'abc'))  # True
print(compare_strings('abc', 'abcd'))  # True
print(compare_strings('bc', 'abc'))  # True
print(compare_strings('axc', 'abc'))  # True
print(compare_strings('abc', 'acb'))  # False
print(compare_strings('abc', 'a'))  # False
print(compare_strings('', '   '))  # False
