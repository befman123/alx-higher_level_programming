#!/usr/bin/python3
"""A module with a class and attribute"""


class Square:
    """A class square with size private attribute

    Attributes:
        size (int): the size of one side of a square
    """
    __size = 0

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be {0} 0".format(">="))
        else:
            self.__size = size

    def area(self):
        """Calculates the area of a square
        Returns:
            the area of the square
        """
        return self.__size ** 2


if __name__ == "__main__":
    a = Square(5)
    print("{0}".format(a.area()))
