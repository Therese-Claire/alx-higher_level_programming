#!/usr/bin/python3ii
def square_matrix_simple(matrix=[]):
    new_matrix = [[0] * len(row) for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
