
# создаем my_set
my_set = {0}
print(my_set)

# вызов my_set[0] приведет к ошибке
# TypeError: 'set' object does not support indexing

# добавляем элемент
# Вывод: {1, 2, 3}
my_set.add(2)
print(my_set)

# добавляем несколько элементов
# Вывод: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# добавляем список и множество
# Вывод: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)