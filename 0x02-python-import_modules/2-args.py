#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv) - 1
    if a == 1:
        print("{} argument:" .format(a))
    elif a == 0:
        print("{} aguments." .format(a))
    else:
        print("{} arguments:" .format(a))
    k = 0
    for i in range(a):
        k += 1
        print("{}: {}" .format(k, argv[i + 1]))
