#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        if ord(i) >= 97 and ord(i) <= 122:
            i = ord(i)
            i -= 32
            i = chr(i)
        print("{:s}" .format(i), end="")
    print("")
