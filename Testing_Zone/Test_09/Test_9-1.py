#! /usr/bin/python

d = []
for i in range(1, 11):
    if i % 2 == 0:
        d.append(i * i)
    else:
        d.append(i ** 3)
print(d)

print([i ** 3 if i % 2 else i * i for i in range(1, 11)])
