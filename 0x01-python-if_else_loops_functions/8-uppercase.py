#!/usr/bin/python3
def uppercase(str):
    for i in enumerate(str):
        i = ord(i)
        i -= 32
        i = chr(i)
        print("{}" .format(i))
