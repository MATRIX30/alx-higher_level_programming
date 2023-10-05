#!/usr/bin/python3
""" This is the module for a  function that divides every
    element of matrix by div

"""


def matrix_divided(matrix, div):
    """this function divides every element in a matrix by nubmer div

    Args:
        matrix (list): list of list of int/float
        div (int): nubmer to use as divisor

    """
    size_of_item = len(matrix[0])
    res = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        tmp = []
        if len(i) != size_of_item:
            raise TypeError("Each row of the matrix must"
                            " have the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                )
            tmp.append(round(j / div, 2))
        res.append(tmp)
    return res
