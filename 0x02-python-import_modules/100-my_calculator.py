#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{} {} {} = {}" .format(a, b, argv[2], add(a, b)))
    elif argv[2] == "-":
        print("{} {} {} = {}" .format(a, b, argv[2], sub(a, b)))
    elif argv[2] == "*":
        print("{} {} {} = {}" .format(a, b, argv[2], mul(a, b)))
    elif argv[2] == "/":
        print("{} {} {} = {}" .format(a, b, argv[2], mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
