#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    j = 0
    for i in my_list:
        j += 1
        if i > my_list[a - j]:
            break
            return i
        else:
            continue 
