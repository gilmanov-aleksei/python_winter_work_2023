#! /usr/bin/python

f = open('test.txt', 'w')
for i in range(10):
    f.write(f"{i}' {i * i}: ")

f.close()
