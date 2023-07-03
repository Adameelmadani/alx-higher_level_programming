#!/usr/bin/python3

"""
This is div module
"""


def matrix_divided(matrix, div):
    """
    This function devide matrix by div
    """

    typeErr = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list)) or (len(matrix) != 2):
        raise TypeError(typeErr)
    for sub_mat in matrix:
        for li in sub_mat:
            if not type(li) in [int, float]:
                raise TypeError(typeErr)
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    my_mat = [[], []]
    for i in range(2):
        for li in matrix[i]:
            number = round(li / div, 2)
            if number == int(number):
                number = int(number)
            my_mat[i].append(number)
    return (my_mat)


if __name__ == "__main__":
    import doctest
    """
    This is doctest module
    """
    doctest.testfile("./tests/2-matrix_divided.txt")
