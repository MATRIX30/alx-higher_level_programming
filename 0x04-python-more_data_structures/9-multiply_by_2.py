#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    if a_dictionary:
        for key in a_dictionary:
            res[key] = a_dictionary[key] * 2
    return res
