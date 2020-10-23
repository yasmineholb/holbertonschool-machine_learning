#!/usr/bin/env python3
""" definiteness """
import numpy as np


def definiteness(matrix):
    """ Function that calculates
        the definiteness of a matrix """
    trans = np.transpose(matrix)
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix == []:
        return None
    if len(matrix.shape) != 2 or not np.array_equal(trans, matrix):
        return None
    if len(matrix[0]) != len(matrix[1]):
        return None
    d, c = np.linalg.eig(matrix)
    s1 = []
    s2 = []
    s3 = []
    for i in range(len(d)):
        if d[i] < 0:
            s1.append(d[i])
        if d[i] == 0:
            s2. append(d[i])
        if d[i] > 0:
            s3.append(d[i])
    if len(s1) == 0 and len(s2) == 0 and len(s3) > 0:
        return("Positive definite")
    elif len(s1) == 0 and len(s2) > 0 and len(s3) > 0:
        return("Positive semi-definite")
    elif len(s1) > 0 and len(s2) > 0 and len(s3) == 0:
        return("Negative semi-definite")
    elif len(s1) > 0 and len(s2) == 0 and len(s3) == 0:
        return("Negative definite")
    elif len(s1) > 0 and len(s2) == 0 and len(s3) > 0:
        return("Indefinite")
    else:
        return(None)
