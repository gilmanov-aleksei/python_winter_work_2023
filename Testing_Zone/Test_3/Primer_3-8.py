#! /usr/bin/python

def result(num_my):

    num = [54,24,34,1,2,3]
    num_res = []

    for number in num:
        if number in num_my:
            num_res.append(number)
    return num_res
num_1 = (result([54,24,1,2,3]))
num_2 = (result([34,1,3]))

print(num_1)
print(num_2)