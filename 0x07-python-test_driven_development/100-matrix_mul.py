#!/usr/bin/python3

"""
This is multiplication module
"""


def matrix_mul(m_a, m_b):
    """
    This is matrix_mul function
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    my_list = [[]]
    if type(m_a) is not type(my_list):
        raise TypeError("m_a must be a list of lists")
    if type(m_b) is not type(my_list):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    a = 0
    s = 0
    for j in m_a:
        if j == m_a[0]:
            s = len(j)
        elif len(j) != s:
            a = 1
        for i in j:
            if not type(i) in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    b = 0
    for j in m_b:
        if j == m_b[0]:
            s = len(j)
        elif len(j) != s:
            b = 1
        for i in m_b:
            if not type(i) in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    if a == 1:
        raise TypeError("each row of m_a must be of the same size")
    if b == 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


if __name__ == "__main__":
    import doctet
    """
    doctest module
    """
    doctest.testfile("./tests/100-matrix_mul.txt")
