#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)
    for i in range(0, len(matrix)):
        if matrix[i] is None:
            continue
        for j in range(0, len(matrix[i])):
            if j == (len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end="")
                continue
            print("{:d} ".format(matrix[i][j]), end="")
        print("")
