#! /usr/bin/python

# try:
#     file = open('ok123.txt', 'r')
# except FileNotFoundError as e:
#     print(FileNotFoundError, e)
# except Exception as e:
#     print(Exception, e)
#

# def divide(x, y):
#     try:
#         out = x / y
#     except:
#         try:
#             import math
#             out = math.inf * x / abs(x)
#         except:
#             out = None
#     finally:
#         return out
#
#
# print(divide(0, 0))

# try:
#     raise Exception("Что-то пошло не так")
# except Exception as e:
#     print("Message:" + str(e))

# def validate(name):
#     if len(name) < 10:
#         raise ValueError
#
#
# try:
#     name = input("Enter Name:")
#     validate(name)
# except ValueError:
#     print("Name is short")
#
# class NameTooShortError(ValueError):
#     pass
#
#
# def validate(name):
#     if len(name) < 10:
#         raise NameTooShortError
# #
# class Positive(ValueError): pass
#
#
# class Negative(ValueError): pass
#
#
# def fun(lst):
#     for x in lst:
#         try:
#             if x == 0:
#                 print(0)
#             elif x > 0:
#                 raise Positive
#             else:
#                 raise Negative
#         except Positive:
#             print("Положительное")
#         except Negative:
#             print("Отрицательное")
#
#
# lst = [0, -15, 1, 1.5, - 2.7, 5, 0, 34, -56]
# print(fun(lst))
