#!/usr/bin/python3
from add_0 import add


def my_add():
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a,b)}")


if (__name__=="__main__"):
    my_add()
