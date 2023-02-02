#! /usr/bin/python

def code(string, n):
    chif = ""
    for i in string:
        if 65 <= ord(i) <= 90:
            chif += chr((ord(i) + n - 65) % 26 + 65)
        elif 97 <= ord(i) <= 122:
            chif += chr((ord(i) + n - 97) % 26 + 97)
        else:
            chif += i
    return chif

txt = str(input("Enter string: "))
step = int(input("Enter step: "))
print(code(txt, step))
print(txt)
