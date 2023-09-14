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
    while i + 1 < len(roman_string):
        if len(roman_string) == 1:
            return roman_to_int_dict[roman_string[i]]
        if (roman_to_int_dict[roman_string[i]] < roman_to_int_dict[roman_string[i+1]]):
            res -= roman_to_int_dict[roman_string[i]]
        else:
            res += roman_to_int_dict[roman_string[i]]
        i +=1
    return res
