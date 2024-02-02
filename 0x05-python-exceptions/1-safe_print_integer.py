#!/usr/bin/python3
def safe_print_integer(value):
    int_test = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        int_test = False
    return int_test
