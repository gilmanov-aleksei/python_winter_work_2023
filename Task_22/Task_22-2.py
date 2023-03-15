#! /usr/bin/python

# Задача 22-2
# Дана структура типа бинарное дерево. Все вершины пронумерованы от 1 до n.
# Дерево задано в виде списка кортежей:
# [(1,2),(1,3),(2,4),(2,5),(3,6),(6,7),(17,8)].
# Каждый кортеж (a,b) показывает, что вершина a соединена с вершиной b.
# По определению в дереве невозможны циклы.
# Найти максимальную длину от вержины (1) до конечной вершины.


tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (17, 8)]

# Создаем словарь, который будет хранить дочерние вершины каждой вершины
children = {}
for edge in tree:
    parent, child = edge
    if parent not in children:
        children[parent] = []
    children[parent].append(child)


# Рекурсивно находим максимальную глубину дерева
def find_max_depth(node):
    if node not in children:
        return 0
    depths = [find_max_depth(child) for child in children[node]]
    return max(depths) + 1


max_depth = find_max_depth(1)  # Начинаем с корня

print("Максимальная длина пути от корня до листа: ", max_depth)
