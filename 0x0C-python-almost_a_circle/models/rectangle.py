#!/usr/bin/python3
""" Module for the class Rectangle
    The class rectangle inherits from
    base in base.py
"""
import base


class Rectangle(base.Base):
    """ The class Rectangle

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method

            Arguments:
                width: integer value assigned to width
                height: integer value assigned to height
                x: integer value assigned to x
                y: integer value assigned to y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be {} 0".format(">"))
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be {} 0".format(">"))
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be {} 0".format(">="))
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be {} 0".format(">="))
        else:
            self.__y = value


if __name__ == "__main__":
    pass
