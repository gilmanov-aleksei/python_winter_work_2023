#! /usr/bin/python


#
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         val = func(*args, **kwargs)
#         end = time.perf_counter()
#         work_time = end - start
#         print(f'Время выполнения {func.__name__}:{round(work_time, 4)} сек.')
#         return val
#
#     return wrapper
#
#
# @timer
# def test(n): return sum([i ** 2 for i in range(n)])
# @timer
# def sleep(n): time.sleep(n)
#
# res1 = test(10000)
# res2 = sleep(4)
# print(f'Результат функции test = {res1}')
# print(f'Результат функции test = {res2}')

def decorator(func):
    def wrapper(*args, **kwargs):
        z = func(*args)
        res = ''.join(args)
        return res

    return wrapper


@decorator
def aaa(*args):
    print(aaa.__name__)
    return
print(aaa('xxx', 'yyy', 'zzz'))
@decorator
def bbb(x, y):
    print(bbb.__name__)
    return len(x) + len(y)
print(bbb('Hello', 'world'))
