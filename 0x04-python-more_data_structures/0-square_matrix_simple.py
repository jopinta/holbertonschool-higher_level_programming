#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in range(0, len(matrix)):
        new_matrix.append([])
        for j in range(0, len(matrix[i])):
            new_matrix[i].append(j)
            new_matrix[i][j] = matrix[i][j] ** 2

    else:
        raise Exception()
    return new_matrix
