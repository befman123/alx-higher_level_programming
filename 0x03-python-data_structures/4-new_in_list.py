#!/usr/bin/python3
""" Modifies a copy of a list"""


def new_in_list(my_list, idx, element):
    ret = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return ret
    else:
        ret[idx] = element
        return ret


if __name__ == "__main__":
    pass
