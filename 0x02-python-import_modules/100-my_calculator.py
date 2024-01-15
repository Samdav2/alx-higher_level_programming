#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul
if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int (argc[3])
    for i in argv:
        if i == '+':
            print("{} {} {} = {}" .format(a, b, i, add(a, b)))
        elif i == '-':
            print("{} {} {} = {}" .format(a, b, i, sub(a, b)))
        elif i == '*':
            print("{} {} {} = {}" .format(a, b, i, mul(a, b)))
        elif i == '/':
            print("{} {} {} = {}" .format(a, b, i, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
