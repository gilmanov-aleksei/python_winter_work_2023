#! /usr/bin/python

# string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
string = "Hello - World!"
str = ""
n = 3
for i in string:
    if 65 <= ord(i) <=90:
        str += chr(ord(i) + n)
    elif 97 <= ord(i) <= 122:
        str += chr(ord(i) + n)
    else:
        str += i
print (str)


