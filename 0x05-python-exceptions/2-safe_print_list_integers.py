#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in my_list:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (IndexError, TypeError, ValueError):
            print(end="")
        else:
            j += 1
    print()
    return j

