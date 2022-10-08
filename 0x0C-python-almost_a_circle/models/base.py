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
        """ returns the json representaion of
            the list of dictionaries

        Arguments:
            list_dictionaries: the object to serialize
        Returns:
            the serialized list of dictionaries or empty list
            if the list of dictionaries is None or empty
        """
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])

    def save_to_file(cls, list_objs):
        if len(list_objs) != 0  and type(list_objs[0]) is R.Rectangle:
            filename = f"{R.Rectangle.__class__}.json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))


if __name__ == "__main__":
    pass
