#!/usr/bin/python3
""" This module contains the base class
    to inherit from
"""


from fileinput import filename
from genericpath import exists
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

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set

            Arguments:
                **dictionary: can be assumed as a double pointer to
                                a dictionary
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
            obj.update(**dictionary)
            return obj
        elif cls.__name__ == "Square":
            obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """ Creates a list of instances from a json file

            Note:
                The returned list of objects depends on the
                calling class

            Returns:
                A list of instances of a Rectangle or Square
                class
        """
        list_inst = []
        if cls.__name__ == "Rectangle":
            file_name = "Rectangle.json"
        elif cls.__name__ == "Square":
            file_name = "Square.json"

        if exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                list_dict = cls.from_json_string(f.read())
                for dict in list_dict:
                    obj = cls(1, 1)
                    obj = obj.create(**dict)
                    list_inst.append(obj)
        return list_inst

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save objects of the children classes Square and Rectangle

            Note:
                if list_objs is empty or list_dict remains empty, an empty
                file is saved
            Arguments:
                list_objs:  a list of instances of the Rectangle or Square
                            classes
        """
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())

        if cls.__name__ == "Rectangle":
            file_name = "Rectangle.json"
        elif cls.__name__ == "Square":
            file_name = "Square.json"

        with open(file_name, "w", encoding="utf-8") as f:
            if len(list_dict) == 0:
                the_str = ""
            else:
                the_str = cls.to_json_string(list_dict)
            f.write(the_str)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves a list of objects to a <class name>.csv file

            Arguments:
                list_objs: a list of objects to be written to file
        """
        if cls.__name__ == "Rectangle":
            file_name = "Rectangle.csv"
        elif cls.__name__ == "Square":
            file_name = "Square.csv"

        with open(file_name, "w", encoding="utf-8") as f:
            for obj in list_objs:
                if len(list_objs) == 0 or list_objs is None:
                    f.write("")
                if file_name == "Rectangle.csv":
                    f.write(f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}\n")
                elif file_name == "Square.csv":
                    f.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """ Loads from file a list of objects
        """
        if cls.__name__ == "Rectangle":
            file_name = "Rectangle.csv"
        elif cls.__name__ == "Square":
            file_name = "Square.csv"

        list_objs_csv = []
        if exists(file_name):
            with open(file_name, encoding="utf-8") as f:
                for l in f:
                    if file_name == "Rectangle.csv":
                        s = l.split(",", 5)
                        s[4].replace("\n", "")
                        obj = cls(1,1)
                        obj.update(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]))
                        list_objs_csv.append(obj)
                    elif file_name == "Square.csv":
                        s = l.split(",", 4)
                        s[3].replace("\n", "")
                        obj = cls(1)
                        obj.update(int(s[0]), int(s[1]), int(s[2]), int(s[3]))
                        list_objs_csv.append(obj)
        return list_objs_csv


if __name__ == "__main__":
    pass
