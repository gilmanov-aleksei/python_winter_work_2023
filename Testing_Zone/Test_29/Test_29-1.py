#! /usr/bin/python

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(1)
b = Node(22)
c = Node(35)
d = Node(7)
e = Node(15)
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

ma = a.value
print(ma)
x = a
while x.next_node != None:
    if x.value > ma:
        ma = x.value
        print(ma)
    x = x.next_node
print(ma)
