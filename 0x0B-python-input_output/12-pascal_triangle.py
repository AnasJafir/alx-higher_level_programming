#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(n):
    """
    Method that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    lst = []
    if n <= 0:
        return lst
    else:
        lst = [[1]]
        while len(lst) < n:
            last_row = lst[-1]
            new_row = [1]
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row.append(1)
            lst.append(new_row)
        return lst
