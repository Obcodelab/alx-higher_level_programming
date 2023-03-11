#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        char = sentence[0]
    else:
        char = None
    return (length, char)
