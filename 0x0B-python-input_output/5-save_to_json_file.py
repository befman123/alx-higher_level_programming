#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Arguments:
            my_obj: any serializable object
            filename: the file to write the json of my_obj
    """
    with open(filename, "a", encoding="utf-8") as f:
        json.dump(my_obj, f)


if __name__ == "__main__":
    pass
