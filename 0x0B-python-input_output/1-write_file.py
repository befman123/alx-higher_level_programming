#!/usr/bin/python3
"""Writes to a new file"""


def write_file(filename="", text=""):
    """This function does the actual work

    Arguments:
        filename: a string representing the file name
        text: the string to be written to the file
    """
    if filename == "" or filename is None or type(filename) is not str:
        pass
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    pass
