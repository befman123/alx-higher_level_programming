#!/usr/bin/python3
"""Writes to a new file"""


import json


def to_json_string(my_obj):
    """This function does the actual work

    Arguments:
        obj: the object to serialize
    Returns:
        the serialized object
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    pass
