#!/usr/bin/python3
import hidden_4 as h


def my_function():
    list = dir(h)
    for i in range(0, len(list)):
        if list[i].startswith("__"):
            continue
        print("{0}".format(list[i]))
    return


if __name__ == "__main__":
    my_function()
