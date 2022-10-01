#!/usr/bin/python3
"""Removes a character at index from a string"""


def remove_char_at(str, n):
    str_new = ""
    for i in range(0, len(str)):
        if i != n:
            str_new += str[i]


if __name__ == "__main__":
    remove_char_at("befiker", 3)
