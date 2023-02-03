#! /usr/bin/python

s = 'АГЦТАГЦТАГЦТ'
n = 3
d = {}
for i in range(len(s) - n + 1):
    d[s[i:i + n]] = d.get(s[i:i + n], 0) + 1
print(d)
mx = max(d.values())
for i in d:
    if d[i] == mx:
        print(i, mx)


