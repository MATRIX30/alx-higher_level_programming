#!/usr/bin/python3
"""Module to handle matrix multiplication using numpy"""


import numpy as np


def matrix_mul(m_a, m_b):
    """_summary_

    Args:
            m_a (list): list of int/float
            m_b (list): list of int/float
    """
    return np.matmul(m_a, m_b)
