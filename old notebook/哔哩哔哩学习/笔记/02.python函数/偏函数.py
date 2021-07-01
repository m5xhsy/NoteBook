from functools import partial


def add(a, b):
    return a+b


par_func = partial(add, 1, 2)
print(par_func())

par_func = partial(add, 1)
print(par_func(5))