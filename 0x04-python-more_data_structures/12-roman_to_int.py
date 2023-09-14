#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or None:
        return 0
    roman_dict = {
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
    if len(roman_string) == 1:
        return roman_dict[roman_string]
    while i + 1 < len(roman_string):
        if (roman_dict[roman_string[i]] < roman_dict[roman_string[i+1]]):
            res -= roman_dict[roman_string[i]]
        else:
            res += roman_dict[roman_string[i]]
        i += 1
    res += roman_dict[roman_string[i]]
    return res
