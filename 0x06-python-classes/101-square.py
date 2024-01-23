#!/usr/bin/python3
""" Module 0-square.py that defines a Square class"""


class Square:
    """ class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """ We define the size variable as a private instance of the class"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        """A getter method for the property position"""
        return self.__position

    @position.setter
    def position(self, value):
        """a setter method for the property position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

    def my_print(self):
        """prints a square using the # character and fills with
           space according to the value of position
        """
        if self.size == 0:
            print()
        for w in range(0, self.position[1]):
            print()
        for i in range(0, self.size):
            for k in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.size):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """ Returns a string represntaion of this class"""
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
        return the_str


if __name__ == "__main__":
    pass
