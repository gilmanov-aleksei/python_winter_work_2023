#! /usr/bin/python

def nalog(pn, sn=13):
    result = pn * sn / 100
    return result

#while True:
#    x = float(input("Enter many: ").split())
#    if x[0] == 0:
#        break
x = 20000
stav = 15
res = nalog(x, stav)
print("Pod.Nalog: ", res, "Stavka", stav)
