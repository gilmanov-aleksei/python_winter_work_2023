#! /usr/bin/python

# t = int(input())
t = 3661
s = t % 60
m = t // 60
m = m % 60
h = t // 3600
h = h % 3600
d = t // 86400

print(t , "=", h, m ,s)




