#! /usr/bin/python

w1 = 'dkjfaiuyishj  shjdsbmnblkdjlk'
w2 = 'hjghjghgj gyuu!@#$%ygu yguyguygu'
dict_w = {}
dict_w2 = {}
for i in range(len(w1)):
    dict_w[w1[i]] = dict_w.get(w1[i], 0) + 1
print(dict_w)

for i in range(len(w2)):
    dict_w2[w2[i]] = dict_w2.get(w2[i], 0) + 1
print(dict_w2)