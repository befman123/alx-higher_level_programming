#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (abs(i) % 15) == 0:
            print("FizzBuzz", end=" ")
        elif (abs(i) % 5) == 0:
            print("Buzz", end=" ")
        elif (abs(i) % 3) == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(i), end=" ")
