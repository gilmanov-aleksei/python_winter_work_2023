#! /usr/bin/python

f = open("text.txt", 'r+t', encoding='utf-8')
print(f.read())
f.write("Hello\n")
print(f.write())

f.close()
