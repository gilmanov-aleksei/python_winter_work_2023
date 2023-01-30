
def uni_let(lst):
    tes = set()
    for i in lst:
        tes = tes.union(i)
    print(tes)
    sortes = sorted(tes)
    string = ''.join(sortes)
    return string, len(string)

print(uni_let(['Hello', 'world']))


