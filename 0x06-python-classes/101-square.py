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

    @property
    def size(self):
        """Returns the value private instance variable size"""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter for the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __str__(self) -> str:
        """ Return string representation of this class"""
        the_str = ""
        if self.size == 0:
            the_str += "\n"
        for w in range(0, self.position[1]):
            the_str += "\n"
        for i in range(0, self.size):
            for k in range(0, self.position[0]):
                the_str += " "
            for j in range(0, self.size):
                the_str += "#"
            the_str += "\n"


if __name__ == "__main__":
    pass
