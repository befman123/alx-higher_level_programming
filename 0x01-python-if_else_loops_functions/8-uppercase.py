#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str1 += chr(ord(str[i]) - 32)
        else:
            str1 += str[i]
    return str1
