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
    new_list = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        lst = []
        if type(i) is not list:
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        if(len(matrix[0]) != len(i)):
            raise TypeError("Each row of the matrix\
 must have the same size")
        for j in range(len(i)):
            if (type(i[j]) is not int) and (type(i[j]) is not float):
                raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
            lst.append(round(((i[j]) / div), 2))
        new_list.append(lst)
    return new_list
