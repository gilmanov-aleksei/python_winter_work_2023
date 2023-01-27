#! /usr/bin/python

primer = input().split()
dict_w = {}
    # Подсчитываем каждый символ w1 в словаре.
    for i in range(len(w1)):
        dict_w[w1[i]] = dict_w.get(w1[i], 0) + 1