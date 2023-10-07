#!/usr/bin/python3
"""Module to handle matrix multiplication using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function to multiply 2 matrices m_a and m_b

    Args:
            m_a (list): list of  list of int/float
            m_b (list): list of list of int/float
    """
    return np.matmul(m_a, m_b)
