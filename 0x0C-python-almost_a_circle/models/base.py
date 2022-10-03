#!/usr/bin/python3
""" This module contains the base class
    to inherit from
"""


class Base:
    """Class base

    Attributes:
        id: a public instance variable intger value
        __nb_objects: a protected variable integer value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Obviously the class instantiation method

        Arguments:
            id: possible value of the private instance
                variable id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


if __name__ == "__main__":
    pass
