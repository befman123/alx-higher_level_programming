#!/usr/bin/python3
"""Prints alphabets in reverse order"""


def func():
    for j in map(mp_func, range(0, 26).__reversed__()):
        print("{0}".format(chr(j)), end="")


def mp_func(j):
    if j == 0 or j % 2 == 0:
        return (j + 65)
    else:
        return (j + 97)


if __name__ == "__main__":
    func()
