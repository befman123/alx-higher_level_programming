#!/usr/bin/python3
""" This module has a function that prints
    the elements of an integer list
"""


def print_list_integer(my_list=[]):
    for el in my_list:
        print("{0}".format(el))


if __name__ == "__main__":
    print_list_integer([1, 2, 3, 4, 5])