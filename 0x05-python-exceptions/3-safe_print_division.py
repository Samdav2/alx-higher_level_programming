#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
       a / b
    except ZeroDivisionError:
        return None
    else:
        c = a / b
        return c
    finally:
        print("Inside Result: {}".format(c))
