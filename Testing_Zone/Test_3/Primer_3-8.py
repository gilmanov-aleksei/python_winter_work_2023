out, mx = 0, 0
for cur in map(lambda c: {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}[c], input("Enter: ")[::-1]):
    if cur >= mx: out, mx = out + cur, cur
    else: out -= cur
print(out)