
n = input(" Enter a word: ").split()
tes = set()
for i in n:
    tes = tes.union(i)
print(len(tes))

