#! /usr/bin/python

# try:
#     file = open('ok123.txt', 'r')
# except FileNotFoundError as e:
#     print(FileNotFoundError, e)
# except Exception as e:
#     print(Exception, e)
#

def divide(x, y):
    try:
        out = x / y
    except:
        try:
            import math
            out = math.inf * x / abs(x)
        except:
            out = None
    finally:
        return out


print(divide(0, 0))
