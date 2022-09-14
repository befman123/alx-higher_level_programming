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

        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or position[1] < 0:
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
            for l in range(0, self.position[1]):
                    print()
            for i in range(0, self.size):
                for w in range(0, self.position[0]):
                    print("{0}".format(" "), end="")
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
        error_string = "position must be a tuple of 2 positive integers"
        if value is None:
            return self._position
        elif len(value) != 2:
            raise TypeError(error_string)
        elif type(value) is not tuple:
            raise TypeError(error_string)
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError(error_string)
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError(error_string)
        else:
            self._position = value

    size = property(size, size)
    position = property(position, position)


if __name__ == "__main__":
    b = Square(1,(1,))
