#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def checker(num):
    global number
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    elif num < 6 and num != 0:
        print(f"Last digit of {number} is {num} and is less than 6 and not 0")


if number < 0:
    last_digit = (number*-1) % 10
    if last_digit > 0:
        last_digit *= -1
        checker(last_digit)
    else:
        print(f"Last digit of {number} is {last_digit} and is 0")
elif number == 0:
    last_digit = number % 10
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    last_digit = number % 10
    checker(last_digit)
