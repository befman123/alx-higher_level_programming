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

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    size = property(size, size)


if __name__ == "__main__":
    a = Square(5)
    b = Square(3)
    print(a > b)
