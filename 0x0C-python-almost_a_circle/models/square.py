#!/usr/bin/python3
""" module square contains class square
    that inherits from rectangle
"""


from . import rectangle


class Square(rectangle.Rectangle):
    """ class square inherits everything from
        class Rectabgle in recy=tangle module

        Note:
            A Square is a rectangle where width
            and height are the same
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        s = f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        return s

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


if __name__ == "__main__":
    pass
