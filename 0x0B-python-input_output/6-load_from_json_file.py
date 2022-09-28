#!/usr/bin/python3
"""Loads an object from a python file"""


import json


def load_from_json_file(filename):
    """Loads an object from a python file

    Arguments:
        filename: the file to read json objects from
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    pass
