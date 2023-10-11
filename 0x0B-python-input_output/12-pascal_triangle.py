#!/usr/bin/python3
"""Technical interview preparation
module for a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """function to print pascal triangle
    Args:
            n(int): number to print pascal triangle
    """
    # test if n is <= 0 and return empty list
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [[1], [1, 1]]

    res = [[1], [1, 1]]
    for i in range(2, n):
        new_item = []
        k = 0
        for j in range(i):
            if j == 0:
                new_item.append(1)
                continue
            new_item.append(res[i - 1][k] + res[i - 1][k + 1])
            k = k + 1
        new_item.append(1)
        res.append(new_item[:])
    return res
