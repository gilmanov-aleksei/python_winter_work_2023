

#str1 = list(input())
s = "apple"

str1 = list(s)
# if abs(len(vow) - len(cons)) <=1
#glas = {1:'a', 2:'e', 3:'i', 4:'o', 5:'u'}
#sogl = {}
glas  = ['a', 'e', 'i', 'o', 'u']
sogl = []
g = 0
s = 0
for i in range(len(str1)):
    for j in range(len(glas)):
        if str1[i] == glas[j]:
            g += 1
    if str1[i] != glas[j]:
        s += 1
print(g, "-", s)


# print(''.join(out))