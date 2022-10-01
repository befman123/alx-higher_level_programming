#!/usr/bin/python3
"""Prints numbers from 1 - 100
   if divisible by 3 print fizz
   if divisible by 5 print buzz
   if both print fizzbuzz
"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{0}".format("FizzBuzz"), end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{0}".format(i), end=" ")


if __name__ == "__main__":
    fizzbuzz()
