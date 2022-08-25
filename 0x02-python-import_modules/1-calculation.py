#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def my_calculator():
    a = 10
    b = 5
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    print("{0} / {1} = {2}".format(a, b, div(a, b)))
    return


if (__name__ == "__main__"):
    my_calculator()
