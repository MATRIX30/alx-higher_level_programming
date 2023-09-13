#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    if matrix:
        for items in matrix:
            res.append(list(map((lambda x: x*x), items)))
    return res
