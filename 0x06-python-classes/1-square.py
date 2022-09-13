#!/usr/bin/python3
"""A module with a class and attribute"""


class Square:
    """A class square with size private attribute

    Attributes:
        size (float): the size of one side of a square
    """
    __size = 0.0

    def __init__(self, size=0.0):
        self.__size = size


if __name__ == "__main__":
    a = Square()
