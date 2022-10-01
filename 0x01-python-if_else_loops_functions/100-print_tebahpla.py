#!/usr/bin/python3
"""Prints alphabets in reverse order"""


def func():
    for i, j in zip(range(0, 26).__reversed__(), range(65, 91).__reversed__()):
        if j % 2 == 0:
            print(chr(j), end="")
        else:
            print(chr(j + 32), end="")


if __name__ == "__main__":
    func()
