#!/usr/bin/python3
import sys as s


def my_function():
    sum = 0
    for i in range(1, len(s.argv)):
        sum = sum + int(s.argv[i])
    print(sum)
    return


if __name__ == "__main__":
    my_function()
