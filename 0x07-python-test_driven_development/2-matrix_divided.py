#!/usr/bin/python3
"""matrix_divided Module"""


def matrix_divided(matrix, div):
    """Method that divides elements of matrix"""
    if type(matrix) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    elif type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        divided = []
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in matrix[i]:
            result = elem/div
            divided.append(round(result, 2))
        new_matrix.append(divided)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
