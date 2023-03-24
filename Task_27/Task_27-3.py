#! /usr/bin/python

# Задача 27-3
#
# Дан список.
# Посчитайте сколько в нем элементов, включая вложенные списки.
# Например:
# [] -->0
# [1, 2, 3] -->3
# ["x", "y", ["z"]] -->4
# [1, 2, [3, 4, [5]]] -->7

def count_elm(lst):
    # Переменная для подсчета элементов
    count = 0
    # Цикл по списку всех элементов
    for x in lst:
        # Если элемент является списком,
        if type(x) == list:
            # увеличиваем переменную на 1
            count += 1
            # рекурсия для перебора вложенных списков
            count += count_elm(x)
        # Если элемент не является списком,
        else:
            # увеличиваем переменную на 1
            count += 1
    return count


print(count_elm([]), ' --> []', " --> 0")
print(count_elm([1, 2, 3]), ' --> [1, 2, 3]', " --> 3")
print(count_elm(["x", "y", ["z"]]), ' --> ["x", "y", ["z"]]', "--> 4")
print(count_elm([1, 2, [3, 4, [5]]]), ' --> [1, 2, [3, 4, [5]]]', " --> 7")

print("Вариант из интернета")


def count_elements(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += 1
            count += count_elements(item)
        else:
            count += 1
    return count


print(count_elements([]))  # 0
print(count_elements([1, 2, 3]))  # 3
print(count_elements(["x", "y", ["z"]]))  # 4
print(count_elements([1, 2, [3, 4, [5]]]))  # 7
