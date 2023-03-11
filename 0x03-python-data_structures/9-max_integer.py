#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        new_list = sorted(my_list)
        Max = new_list[-1]
        return Max
