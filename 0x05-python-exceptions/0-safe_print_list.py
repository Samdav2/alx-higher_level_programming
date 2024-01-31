#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(0, x):
        try:
            my_list[i]
        except IndexError:
            print(end="")
        else:
            j += 1
            print("{}" .format(my_list[i]))
    print()
    return j
