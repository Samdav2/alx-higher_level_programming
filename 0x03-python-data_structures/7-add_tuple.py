#!/bin/usr/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < 1:
        add = tuple(a + b for a, b in zip(tuple_a, tuple_b))
    else:
        add = tuple(a + b for a, b in zip(tuple_a, tuple_b))
    return add
