#!/usr/bin/python3
from add_0 import add


def my_add():
    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    return


if (__name__ == "__main__"):
    my_add()
