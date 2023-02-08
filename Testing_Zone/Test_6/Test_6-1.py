#! /usr/bin/python

dct = {1: {11: {111:1111}}, 2: {22: {222:2222}}, 3: {33:333}, 4: 444}
for i in dct:
    print(i, dct[i])
    if type(dct[i]) == dict:
        for j in dct[i]:
            print(j, dct[i][j])
            if type(dct[i][j]) == dict:
                for k in dct[i][j]:
                    print(k, dct[i][j][k])
