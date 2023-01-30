# input n 

text = input("Enter a word: ")
for i in text:
    if i not in 'abcdefghijklmnopqrstuvwxyz':
        text = text.replace(i, ' ')
a = text.split()
for j in a:
    b = 0
    for k in j:
        b += 1 if k in 'aeiouy' else 0
    if b >= 4:
        print(j)
print(a)