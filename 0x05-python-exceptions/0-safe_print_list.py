#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            print(my_list[i], end="")
        except IndexError:
            print("Error", end="")
    print()
ls = ["tefera", 2, 3]
safe_print_list(ls, 4)