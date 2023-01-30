
def nalog(temp):
    result = temp * 13 / 100
    return result

while True:
    x = float(input("Enter coin: "))
    if x == 0:
        break
    res = nalog(x)
    print("Pod.Nalog: ", res)
