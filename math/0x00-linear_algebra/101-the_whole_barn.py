#!/usr/bin/env python3
""" function"""


def matrix_shape(matrix):
    """shape function """
    L = [len(matrix)]
    while type(matrix[0]) == list:
        L.append(len(matrix[0]))
        matrix = matrix[0]
    return L


def add_matrices(mat1, mat2):
    """ Add function """
    m = matrix_shape(mat1)
    if m != matrix_shape(mat2):
        return None
    else:
        lis = []
        if len(m) > 1:
            for sub1, sub2 in zip(mat1, mat2):
                lis.append(add_matrices(sub1, sub2))
        else:
            for i in range(m[0]):
                lis.append(mat1[i] + mat2[i])
    return lis
