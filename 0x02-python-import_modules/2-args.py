#!/usr/bin/python3
import sys as s


def my_function():
    print("{0} arguments:".format(len(s.argv)))
    for i in range(0, len(s.argv)):
        print("{0}: {1}".format((i + 1), s.argv[i]))
    return


if (__name__ == "__main__"):
    my_function()
