#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i not in "Cc":
            return ("".join(i))
