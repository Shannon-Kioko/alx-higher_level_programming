#!/usr/bin/python3
"""
The '101-lazy_matrix_mul' module.
Def a function that multiplies 2 matrices by using the module NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy

    Args:
        m_a (matrix): first input matrix
        m_b (matrix): second input matrix

    Returns:
        matrix: the product of the two matrices.
    """
    return np.matmul(m_a, m_b)
