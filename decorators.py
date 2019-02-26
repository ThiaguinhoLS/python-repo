# -*- coding: utf-8 -*-

def positive_decorator(fn):
    def wrapper(x):
        if x < 0:
            x = abs(x)
        return fn(x)
    return wrapper


@positive_decorator
def show_number(x):
    return x

assert show_number(10) == 10
assert show_number(-10) == 10
