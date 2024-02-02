#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
       a / b
    except ZeroDivisionError:
        c = None
        return c    
    else:
        c = a / b
        return c
    finally:
        print("Inside result: {}".format(c))
