#!/usr/bin/python3
""" This module contains the base class
    to inherit from
"""


import json


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

    def to_json_string(list_dictionaries):
        """This function does the actual work

        Arguments:
            obj: the object to serialize
        Returns:
            the serialized object
        """
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"


if __name__ == "__main__":
    pass
