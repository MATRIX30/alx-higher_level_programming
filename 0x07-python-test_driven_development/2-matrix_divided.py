#!/usr/bin/python3
""" This is the module for a  function that divides every 
    element of matrix by div
    
    
    
    >>> matrix_divided()
    Traceback (most recent call last):
        ...
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
    >>> matrix_divided([[3,4],[4,3]])
    Traceback (most recent call last):
        ...
    TypeError: matrix_divided() missing 1 required positional argument: 'div'
    >>> matrix_divided([[3,4],[3]], 3)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size
    >>> matrix_divided([[1,3,4],[3,5,6]], "alx")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number
    >>> matrix_divided([[1,3,4],[3,5,6]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    >>> matrix_divided([[6,3,4],[3,5,0]], 2)
    [[3.00,1.50,2.00],[1.50,2.50,0.00]]
    >>> matrix_divided("alx", 4)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[6.2,3,4],[3,5.2,0]], 2)
    [[3.10,1.50,2.00],[1.50,2.60,0.00]]

    >>> matrix_divided([[3,4],[4,3]])
    Traceback (most recent call last):
        ...
    TypeError: matrix_divided() missing 1 required positional argument: 'div'
    >>> matrix_divided([[1,3,"alx"],[2,3,4]], 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[]], [[]], 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix_divided() takes 2 positional arguments but 3 were given
    >>> matrix_divided([[]], [[]], 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix_divided() takes 2 positional arguments but 3 were given
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
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        tmp = []
        if len(i) != size_of_item:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if (not isinstance(j, int) and not isinstance(j, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            tmp.append(j/div)
        res.append(tmp)
    return res
