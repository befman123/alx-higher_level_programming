#!/usr/bin/python3
"""Removes all the C's and c's froma string"""


def no_c(my_string):
    ret = ""
    for el in my_string:
        if el == 'c' or el == 'C':
            continue
        else:
            ret += el
    return ret


if __name__ == "__main__":
    pass
