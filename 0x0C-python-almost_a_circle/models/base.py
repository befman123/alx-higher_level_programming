#!/usr/bin/python
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
        self.id = id

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        if id is not None:
            self.id = value
        else:
            __nb_objects += 1
            self.id = __nb_objects


if __name__ == "__main__":
    pass
