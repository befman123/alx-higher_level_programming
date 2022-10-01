#!/usr/bin/python3
"""Prints the given string in all caps"""


def uppercase(str):
    upper_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper_str += chr(ord(i) - 32)
        else:
            upper_str += i
    return upper_str


if __name__ == "__main__":
    pass
