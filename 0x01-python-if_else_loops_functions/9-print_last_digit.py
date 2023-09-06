#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        tmp = -1 * number
    else:
        tmp = number
    while (tmp > 10):
        tmp %= 10
    print(tmp, end="")
    return tmp
