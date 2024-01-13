#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv)
    for i in range(a):
        b = int(argv[i + 1]) + int(argv[i + 1])
        print("{}" .format(b)
