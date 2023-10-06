#!/usr/bin/python3
"""
Module containing a function that divides all element of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide element of matrix number by number.

    matrix: matrix to be divided.
    div: number to divide the matrix.

    Return: A list results.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for lst in matrix:
        if not isinstance(lst, list) or len(lst) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(lst) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in lst:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(i / div, 2) for i in lst] for lst in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
