#! /usr/bin/python


# Задача 22-2
# Дана структура типа бинарное дерево. Все вершины пронумерованы от 1 до n.
# Дерево задано в виде списка кортежей:
# [(1,2),(1,3),(2,4),(2,5),(3,6),(6,7),(7,8)].
# Каждый кортеж (a,b) показывает, что вершина a соединена с вершиной b.
# По определению в дереве невозможны циклы.
# Найти максимальную длину от вершины (1) до конечной вершины.


# Рекурсивно находим максимальную глубину дерева
# def find_max_depth(node, childrens):
#     if node not in childrens:
#         return 0
#     depths = [find_max_depth(child, childrens) for child in childrens[node]]
#     return max(depths) + 1
#
#
# def dict_child(tree):
#     # Создаем словарь, который будет хранить дочерние вершины каждой вершины
#     children = {}
#     for edge in tree:
#         parent, child = edge
#         if parent not in children:
#             children[parent] = []
#         children[parent].append(child)
#     max_depth = find_max_depth(1, children)
#     return max_depth
bin_tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8), (8, 9)]

# print("Максимальная длина от вершины 1 до конечной вершины: ", dict_child(bin_tree))

d = {}
for i, j in sorted(bin_tree):
    d[j] = d.get(i, 0) + 1
print(max(d.values())+1)
print("Максимальная длина от вершины 1 до конечной вершины: ", d[j])