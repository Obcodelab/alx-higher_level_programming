#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]
    result_tuple = (first_element, second_element)
    return result_tuple
