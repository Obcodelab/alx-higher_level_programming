#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if c in chr(i):
            return True
        else:
            return False
