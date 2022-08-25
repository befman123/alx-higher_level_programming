#!/usr/bin/python3
import add_0


def my_add():
    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add_0.add(a, b)))


if (__name__ == "__main__"):
    my_add()
