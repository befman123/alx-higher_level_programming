#!/usr/bin/python3
""" This module defines a class Rectangle"""


class Rectangle:
    """ The class Rectangle

    Args:
    __width: private positive integer
    __height: private postive integer
    """

    def __init__(self, width=0, height=0):

        """ constructor for the rectangle function

        Args:
        width: a positive integer used as a width of a rectangle
        height: a positive integer used as a width of a rectangle

        """
        if height is None:
            return self.__height
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be {0} 0".format(">="))
        else:
            self.__height = height

        if width is None:
            return self.__width
        elif type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be {0} 0".format(">="))
        else:
            self.__width = width

    def height(self, value=None):
        if value is None:
            return self.__height
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be {0} 0".format(">="))
        else:
            self.__height = value

    def width(self, value=None):
        if value is None:
            return self.__width
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be {0} 0".format(">="))
        else:
            self.__width = value

    def area(self):
        """ Calculates the rea of a rectangle

        Returns:
            height multiplied by width
        """
        return self.height * self.width

    def perimeter(self):
        """ Calculates the perimeter of a rectangle

            Return:
                returns the sircumfrance of the rectangle:
                if height or width are zero, return zero
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    height = property(height, height)
    width = property(width, width)


if __name__ == "__main__":
    a = Rectangle(1, 12)
    print(a.width)
    print(a.height)
