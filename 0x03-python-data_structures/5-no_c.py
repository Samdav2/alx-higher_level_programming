#!/usr/bin/python3
def no_c(my_string):
    j = 0
    a = len(my_string)
    new_string = []
    for i in range(a):
        j += 1
        if my_string[i]== "c" or my_string[i] == "C":
            continue
        else:
           new_string.append(my_string[i])
    new2_string = ''.join(new_string)
    return new2_string
