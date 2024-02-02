#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(0, x)
        try:
            print("{:d}".format(my_list[j]), end="")
        except (IndexError, TypeError, ValueError):
            print(end="")
        else:
            j += 1
    print()
    return j

