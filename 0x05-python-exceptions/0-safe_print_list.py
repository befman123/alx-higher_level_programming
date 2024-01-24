#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for a in range(x):
            print(my_list[a], end="")
            a += 1
    except Exception as e:
        pass
    print()
    return (a)
