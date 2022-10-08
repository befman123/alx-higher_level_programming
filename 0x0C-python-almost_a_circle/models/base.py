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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json representaion of
            the list of dictionaries

        Arguments:
            list_dictionaries: the object to serialize
        Returns:
            the serialized list of dictionaries or empty list
            if the list of dictionaries is None or empty
        """
        temp_list = []
        if list_dictionaries is None:
            return json.dumps(temp_list)
        elif len(list_dictionaries) == 0:
            return json.dumps(temp_list)
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Desrializes the json string to a list of
            dictionaries

            Arguments:
                json_string: a json representation of a list of
                                dictionaries

            Returns:
                a list of dictionaries or an empty list(if json_string is
                empty or None) 
        """
        if json_string is None:
            return []
        elif len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)


if __name__ == "__main__":
    pass
