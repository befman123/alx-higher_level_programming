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

    def update(self, *args, **kwargs):
        list_args = ["id", "size", "x", "y"]

        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.__dict__["id"] = args[0]
                elif i == 1:
                    type(self).__dict__["size"].__set__(self, args[1])
                else:
                    self.__dict__[f"_Rectangle__{list_args[i]}"] = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.__dict__["id"] = kwargs["id"]
                elif key == "size":
                    type(self).__dict__["size"].__set__(self, kwargs["size"])
                else:
                    self.__dict__[f"_Rectangle__{key}"] = kwargs[f"{key}"]


if __name__ == "__main__":
    pass
