#! /usr/bin/python

fi = open("test.txt", 'r', encoding='utf-8')
fo = open("test2.txt", 'w', encoding='utf-8')

#lst = f.readlines()
txt = fi.read()
wxt = ''
print(txt)
for i, j in enumerate(txt):
    if i % 2 == 0:
        wxt +=j
print(wxt)


fo.close()
fi.close()