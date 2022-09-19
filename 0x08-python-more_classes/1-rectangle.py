#!/usr/bin/python3
""" This module defines a class Rectangle"""


class Rectangle:
    """ The class Rectangle

    Args:
    width: private positive integer
    height: private postive integer
"""

    def __init__(self, width=0, height=0):

        """ constructor for the rectangle function

        Args:
        width: a positive integer used as a width of a rectangle
        height: a positive integer used as a width of a rectangle

        """
        self.height(height)
        self.width(width)

    def height(self, height=None):
        if height is None:
            return __height
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be {0} 0".format(">="))
        else:
            self.__height = height

    def width(self, width=None):
        if width is None:
            return self.__width
        elif type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be {0} 0".format(">="))
        else:
            self.__width = width


if __name__ == "__main__":
    a = Rectangle()
