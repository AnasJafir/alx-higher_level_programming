#!/usr/bin/python3
"""
12-pascal_triangle module
"""


def pascal_triangle(n):
    """
    pascal_triange - returns a list of lists of integers
    representing the Pascals triangle of n
    Args:
        n: number of lists
    Return: list of lists
    """
    lst = []
    if n <= 0:
        return lst
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                lst.append([1])
            elif j == i:
                lst[i].append(1)
            else:
                lst[i].append(lst[i - 1][j] + lst[i - 1][j - 1])
    return lst
