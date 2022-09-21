#!/usr/bin/python3
""" This module defines a class Rectangle"""


class Rectangle:
    """ The class Rectangle

    Args:
    __width: private positive integer
    __height: private postive integer
    number_of_instances: a public class varible that is incremented
                            at __init__ and decrenmented at __del__
    print_symbol: a public class variable that stores the value to be printed
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """ constructor for the rectangle function

        Args:
        width: a positive integer used as a width of a rectangle
        height: a positive integer used as a height of a rectangle

        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be {0} 0".format(">="))
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
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

    def __str__(self):
        s = ""
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                s = s + str(Rectangle.print_symbol)
            if i != self.height - 1:
                s = s + "\n"
        return s

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of a rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of a rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2


if __name__ == "__main__":
    Rectangle.print_symbol = "C"
    myrectangle1 = Rectangle(8, 4)
    print(myrectangle1)
