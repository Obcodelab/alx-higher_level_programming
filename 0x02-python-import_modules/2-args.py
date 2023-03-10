#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv[1:]
    input_length = len(user_input)
    if input_length == 0:
        print("0 arguments.")
    elif input_length == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(input_length))
    for position, word in enumerate(user_input):
        print("{:d}: {:s}".format(position + 1, word))
