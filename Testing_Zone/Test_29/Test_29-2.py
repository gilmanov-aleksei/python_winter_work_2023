#! /usr/bin/python

# s = "Используя стек, напечатайте этот список в обратном порядке"
# lst = list(s)
# while True:
#     print(lst.pop(), end='')
#

# s = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#      [11, 12, 13, 14, 15]]
s = []


def push_s(i):
    if not s:
        s.append([])
        s[-1].append(i)
    else:
        if len(s[-1]) < 10:
            s[-1].append(i)
        else:
            s.append([])
            s[-1].append(i)

    return


def pop_s():
    if not s:
        return "Тарелок нет"
    else:
        if len(s[-1]) > 1:
            return s[-1].pop()
        else:
            x = s[-1].pop()
            s.pop()
            return x


for i in range(1, 15):
    push_s(i)
    print(s)
for _ in range(10):
    i = pop_s()
    print(s)
