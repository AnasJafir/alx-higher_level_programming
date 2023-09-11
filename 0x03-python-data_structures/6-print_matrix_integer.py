#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for coln in range(len(row)):
            print("{:d}".format(row[coln]),
                  end=' ' if coln < len(row) - 1 else '')
        print()
