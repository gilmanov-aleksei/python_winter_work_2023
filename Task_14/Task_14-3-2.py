# #! /usr/bin/python

def tri(n):
    if n == 1:
        print('*'.center(10))
    else:
        print(('* ' * n).center(10))
        tri(n - 1)
        print(('* ' * n).center(10))


tri(5)

# def tri_2_2(n):
#     if n > 1:
#         print(('* ' * n).center(n - 2 * n))
#         tri_2_2(n - 1)
#     return print(('* ' * n).center(n - 2 * n))
#
#
# def tri_2_3(n):
#     if n > 0: print(('* ' * n).center(10)) or tri_2_3(n - 1) or print(('* ' * n).center(10))
#     return
#
#
# tri_2_2(5)
# input("Press Enter")
# tri_2_3(5)


