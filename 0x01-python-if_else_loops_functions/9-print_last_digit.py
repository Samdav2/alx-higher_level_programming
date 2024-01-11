#!/usr/bin/python3
def print_last_digit(number):
    i = str(number)
    i = i[-1]
    i = int(i)
    print("{}" .format(i), end="")
    return i
