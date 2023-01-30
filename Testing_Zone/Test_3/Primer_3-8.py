
def convert_to_clsius(temp):
    result = (5/9) * (temp - 32)
    return result

x = convert_to_clsius(32)
print(x)

def convert_to_farengat(temp):
    res_f = temp * (5/9) + 32
    return res_f

y = convert_to_farengat(10)
print(y)