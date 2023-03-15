#! /usr/bin/python

dict1 = {'A': 100, 'B': 200, 'C': 300}
dict2 = {'A': 200, 'D': 200, 'C': 100}

res = {}
for key in dict1 | dict2:
    res[key] = dict1.get(key, 0) + dict2.get(key, 0)
    print(key, res[key], dict1.get(key, 0), dict2.get(key, 0))
print(res)
