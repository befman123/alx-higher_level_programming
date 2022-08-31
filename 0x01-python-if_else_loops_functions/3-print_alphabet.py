#!/usr/bin/python3
def print_alphabet():
    for i in range(97, 123):
        if i != 113 and i != 101:
            print("{0}".format(chr(i)), end="")


if __name__ == "__main__":
    print_alphabet()
