#!/usr/bin/python3
"""A module with a class and attribute"""


class Square:
    """A class square with size private attribute

    Attributes:
        size (int): the size of one side of a square
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be {0} 0".format(">="))
        else:
            self._size = size
        l1 = type(position) is not tuple
        l2 = type(position[0]) is not int
        l3 = type(position[1]) is not int
        l4 = position[0] < 0
        l5 = position[1] < 0
        if (((l1 or l2) or l3) or l4) or l5:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = position

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

    def position(self, value=None):
        """A setter for the private size position
        Args:
            value: the value to set to position
        """
        if value is None:
            return self._position
        l1 = type(value) is not tuple
        l2 = type(value[0]) is not int
        l3 = type(value[1]) is not int
        l4 = value[0] < 0
        l5 = value[1] < 0
        if (((l1 or l2) or l3) or l4) or l5:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    size = property(size, size)
    position = property(position, position)


if __name__ == "__main__":
    a = Square()
