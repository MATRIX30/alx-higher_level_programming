#!/usr/bin/python3

def safe_print_division(a: int, b: int)-> float:
    try:
        res = a / b
    except ZeroDivisionError as z:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
        