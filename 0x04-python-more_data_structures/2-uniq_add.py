#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list:
        res = list(set(my_list))
        for i in res:
            sum += i
    return sum
