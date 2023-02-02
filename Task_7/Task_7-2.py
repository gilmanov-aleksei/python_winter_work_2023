#! /usr/bin/python

def code(string, n):
    chif = ""
    for i in string:
        if 65 <= ord(i) <=90:
            if ord(i) + n > 90:
                chif += chr((ord(i) + n - 64) % 26 + 65)
            else:
                chif += chr(ord(i) + n)
        elif 97 <= ord(i) <= 122:
            if ord(i) + n > 122:
                chif += chr((ord(i) + n - 96) % 26 + 97)
            else:
                chif += chr(ord(i) + n)
        else:
            chif += i
    return chif

# str = input("Enter striing: ")
str = "Zz - XHJVSJghb,dshgdjh. (hgwhgw) kjhGKJWSGWYgyx - 1212 b98d78c7yvvY - zxy!"
# step = int(input("Enter step: "))
step = 3

print(code(str, step))
