#!/bin/usr/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < 1:
        for a, b in zip(tuple_a, tuple_b):
            if a < 0:
                tuple_a = 0
            elif < 0:
                tuple_b = 0
            else:
                add = tuple(a + b)
    else:
        add = tuple(a + b for a, b in zip(tuple_a, tuple_b))
    return add
