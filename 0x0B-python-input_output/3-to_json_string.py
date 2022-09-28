#!/usr/bin/python3
import json as j
"""Writes to a new file"""


def to_json_string(my_obj):
    """This function does the actual work

    Arguments:
        obj: the object to serialize
    Returns:
        the serialized object
    """
    return j.dumps(my_obj)


if __name__ == "__main__":
    pass
