#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    if my_list:
        res = list(set(my_list))
        return (reduce((lambda x, y: x + y), res))
