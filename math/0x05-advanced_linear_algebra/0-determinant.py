#!/usr/bin/env python3
""" determinant """


def determinant(matrix):
    """ Function that calculates the determinant of a matrix """
    len1, len2 = len(matrix), len(matrix[0])
    if len(matrix[0]) == 0 or type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    elif len1 != len2:
        raise ValueError("matrix must be a square matrix")
    if len1 == 1 and len2 == 0:
        return 1
    if len1 == 1 and len2 == 1:
        return matrix[0][0]
        
    
