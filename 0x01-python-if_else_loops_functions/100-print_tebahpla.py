#!/usr/bin/python3
k = 0
for i in range(122, 96, -1):
    k += 1
    if k % 2 == 0:
        i -= 32
        print("{}" .format(chr(i)), end="")
    else:
        print("{}" .format(chr(i)), end="")
