#!/usr/bin/python3
""" Module 0-square.py that defines a Square class"""


class Square:
    """ class Square"""
    def __init__(self, size=0):
        """ We define the size variable as a private instance of the class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2


if __name__ == "__main__":
    pass
