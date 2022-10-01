#!/usr/bin/python3
"""Prints the last digit of a number"""


def print_last_digit(number):
    number = int(number)
    print("{0}".format(number.__abs__() % 10), end="")
    return number.__abs__() % 10


if __name__ == "__main__":
    print_last_digit(-1204)
