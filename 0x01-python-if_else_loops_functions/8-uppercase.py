#!/usr/bin/python3
def uppercase(str):
    for i in range(ord(str)):
        if i not in chr(i) == " ":
            i -= 32
            i = chr(i)
            print("{i}" .format(i))
        else:
            print("{i}" .format(chr(i)))
