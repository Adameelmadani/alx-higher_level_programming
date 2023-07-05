#!/usr/bin/python3

"""
This is multiplication module
"""


def is_two_dimensional(my_list):
    """
    Checking a two_dimensional list
    """
    if isinstance(my_list, list):
        return all(isinstance(element, list) for element in my_list)
    return False


def matrix_mul(m_a, m_b):
    """
    This is matrix_mul function
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if is_two_dimensional(m_a) is False and m_a != []:
        raise TypeError("m_a must be a list of lists")
    if is_two_dimensional(m_b) is False and m_b != []:
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
        for i in j:
            if not type(i) in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    if a == 1:
        raise TypeError("each row of m_a must be of the same size")
    if b == 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """
    Let's multiply now
    """
    m_c = []
    i = 0
    for i in range(len(m_a)):
        my_list = []
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_a[0])):
                c += m_a[i][k] * m_b[k][j]
            my_list.append(c)
        m_c.append(my_list)
    return (m_c)


if __name__ == "__main__":
    import doctet
    """
    doctest module
    """
    doctest.testfile("./tests/100-matrix_mul.txt")
