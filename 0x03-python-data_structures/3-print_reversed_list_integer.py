#!/usr/bin/python3
""" This module has a function that prints
    the elements of an integer list in reverse
"""


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in range(0, len(my_list)).__reversed__():
        print("{:d}".format(my_list[i]))


if __name__ == "__main__":
    print_reversed_list_integer(None)
