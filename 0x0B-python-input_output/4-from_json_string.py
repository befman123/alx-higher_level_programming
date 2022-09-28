#!/usr/bin/python3
"""Converts a JSON reresentation to object"""


import json


def from_json_string(my_str):
    """Does the actual work

    Arguments:
        my_str: the JSON reresentation string to be
                deserialized
    Returns:
        the object deserialized frm my_str
    """
    return json.loads(str(my_str))


if __name__ == "__main__":
    pass
