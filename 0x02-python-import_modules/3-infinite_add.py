#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv) - 1
    b = 0
    for i in range(a):
        b += int(argv[i + 1])
    print("{}" .format(b))
