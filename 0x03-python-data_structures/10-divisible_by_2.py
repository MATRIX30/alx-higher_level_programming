#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for item in my_list:
        if (item % 2 == 0):
            res.append(True)
        res.append(False)
    return res
