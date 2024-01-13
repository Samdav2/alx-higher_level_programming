#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv) - 1
    if a <= 1:
        print("{} arguement:" .format(a))
    else:
        print("{} arguements:" .format(a))
    k = 0
    for i in range(a):
        k += 1
        print("{}: {}" .format(k, argv[i + 1]))
