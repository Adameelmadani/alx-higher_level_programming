#!/usr/bin/python3

"""
This is our module
"""

import numpy as np
"""
This is numpy modul
"""


def lazy_matrix_mul(m_a, m_b):
    """
    This is matrix multiplication but using the lazy method
    """

    return np.matmul(m_a, m_b)
