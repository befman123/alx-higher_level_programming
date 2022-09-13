#!/usr/bin/python3
"""A module with a class and attribute"""


class Square:
    """A class square with size private attribute

    Attributes:
        size (int): the size of one side of a square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be {0} 0".format(">="))
        else:
            self._size = size

    def area(self):
        """Calculates the area of a square
        Returns:
            the area of the square
        """
        return self._size ** 2

    def my_print(self):
        if self.size != 0:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("{0}".format("#"), end="")
                print("")
        else:
            print("")

    def size(self, value=None):
        """A setter for the private size attribute
        Args:
            value: the value to set to size
        """
        if value is None:
            return self._size
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be {0} 0".format(">="))
        else:
            self._size = value

    size = property(size, size)


if __name__ == "__main__":
    a = Square(0)
    a.my_print()
    a.size = 10
    a.my_print()
