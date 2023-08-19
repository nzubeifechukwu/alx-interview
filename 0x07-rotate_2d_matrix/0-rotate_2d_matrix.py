#!/usr/bin/bash
'''Rotate an n * n 2D matrix 90 degrees clockwise. Rotate in-place (no return).
    Matrix cannot be empty.
'''


def rotate_2d_matrix(matrix):
    '''Rotate @matrix 90 degrees clockwise'''
    (j, k) = (0, len(matrix) - 1)

    while j < k:
        for i in range(k - j):
            (c, r) = (j, k)
            copy = matrix[c][j + i]
            matrix[c][j + i] = matrix[r - i][j]
            matrix[r - i][j] = matrix[r][k - i]
            matrix[r][k - i] = matrix[c + i][k]
            matrix[c + i][k] = copy
        k = k - 1
        j = j + 1
