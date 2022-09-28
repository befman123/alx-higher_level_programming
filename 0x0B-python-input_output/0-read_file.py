#!/usr/bin/python3
"""this module reads a text file and prints
   the content to the standard output
"""


def read_file(filename=""):
    """This function actually does the work

    Arguments:
        filename: a string representing the file name
    """
    if filename == "" or filename is None or type(filename) is not str:
        pass
    else:
        with open(filename, "r+", encoding="utf-8") as f:
            for line in f:
                print(line, end="")


if __name__ == "__main__":
