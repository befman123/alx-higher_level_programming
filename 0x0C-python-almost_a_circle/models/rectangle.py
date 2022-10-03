#!/usr/bin/python3
""" Module for the class Rectangle
    The class rectangle inherits from
    base in base.py
"""
from . import base


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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be {} 0".format(">="))
        else:
            self.__y = value

    def area(self):
        """ Calculates area as width * height

        Returns:
            the area of the rectangle
        """
        return self.height * self.width

    def display(self):
        """ print in stdout the Rectangle instance with
            the character # by taking care of x and y
        """
        for h in range(0, self.height):
            if self.y > 0:
                for xs in range(0, self.x):
                    print(" ", end="")
            for w in range(0, self.width):
                print("#".format("#"), end="")
            print()

    def __str__(self):
        """ Returns string representation as the required
            format"""

        s = f"[Rectangle] ({self.id}) {self.x}/{self.y} -"
        s += f" {self.width}/{self.height}"
        return s

    def update(self, *args, **kwargs):
        """ updates self with *args values

        Arguments:
            *args:  a built in list for acceptting
                    variable number arguments in a
                    function
            **kwargs: need i explain?
        Note:
            Argument order is super important, and
            number of args should be five
        """
        if len(args) == 0:
            self.width = kwargs["width"]
            self.height = kwargs["height"]
            self.x = kwargs["x"]
            self.y = kwargs["y"]
            self.id = kwargs["id"]
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception as e:
                pass


if __name__ == "__main__":
    pass
