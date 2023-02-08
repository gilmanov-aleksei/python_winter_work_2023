#! /usr/bin/python

lst = []
with open('test.txt') as fi:
    for i in fi:
        lst.append(i.strip())
    print(lst)
    with open('test.txt', 'w') as fo:
        for line in lst:
            res = sorted(line.split())
            fo.write(' '.join(res) + '\n')
