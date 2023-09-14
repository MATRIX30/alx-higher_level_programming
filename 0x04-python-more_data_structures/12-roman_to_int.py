#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or None:
        return 0
    roman_to_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 100
    }
    res = 0
    i = 0
    while i < len(roman_string):
        res += roman_to_int_dict[roman_string[i]]
        i +=1
    return res
