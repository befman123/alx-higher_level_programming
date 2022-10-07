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
        """ Object creation method for class square
            Arguments:
                size: positive integer that is assigned to both
                      height and width
                x: assigned to inherited property x
                y: assigned to inherited property y
                id: assigned to inherited instance variable 
                    (from base.Base) id
            Note:
                Only super is called since a square has both height
                and width it's just that they are equal
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ The string representation of this class"""
        s = f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        return s

    @property
    def size(self):
        """ getter method for the property size
            Returns:
                self.width since both height and width are equal
                (if it exists) or self.height(if self.width is None)
        """
        if self.width is not None:
            return self.width
        else:
            return self.height

    @size.setter
    def size(self, value):
        """ setter method for the property size
            Arguments:
                value: int value set to both width and 
                        height accordingly
            
            Note:
                assigning value to rectangles height and width
                will pass through the setters in the parent class
                for the corresponding height and width properties
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the object using *args or **kwargs.
            if *args is empty it tries to use **kwargs

            Note:
                The order of assignment if *args is used is 
                important ["id", "size", "x", "y"] 
        
        """
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
