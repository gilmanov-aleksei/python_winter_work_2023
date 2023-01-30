#! /usr/bin/python

def roma_nubers(r_nums):

    pass

 #   return num_print

str_nums = "MMXXIII, MMXXIV, MCMXVII, MXMLXI, MM, MDXXXLXII"
d_roma = { 'I': 1, 'IV': 4, 'V': 5, 'IX': 9,'X': 10,
            'XL': 40,'L': 50, 'XC': 90, 'C': 100,
           'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
           }
str_n = str_nums.split(sep=",")
print(str_n)

for i in str_nums:
#    print(roma_nubers(i))
    print(i, end=" ")
print()

for k, v in d_roma.items():
    print(k, "-", v, end="  ")


