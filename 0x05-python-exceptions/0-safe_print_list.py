#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for a in range(0, x):
        try:
            print(my_list[a], end="")
        except IndexError:
            print("Error", end="")
    print()
    return (a)
