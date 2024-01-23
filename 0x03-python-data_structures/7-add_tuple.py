#!/bin/usr/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp_a = tuple_a + (0, 0)
    tp_b = tuple_b + (0, 0)
    return(tp_a[0] + tp_b[0], tp_a[1] + tp_b[1])
