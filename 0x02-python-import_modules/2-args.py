#!/usr/bin/python3
import sys as s


def my_function():
    if len(s.argv) == 2:
        print("{0} argument:".format((len(s.argv) - 1)))
    elif len(s.argv) == 1:
        print("0 arguments.")
    else:
        print("{0} arguments:".format((len(s.argv) - 1)))
    for i in range(1, len(s.argv)):
        print("{0}: {1}".format(i, s.argv[i]))
    return


if (__name__ == "__main__"):
    my_function()
