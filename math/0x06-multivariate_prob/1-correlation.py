#!/usr/bin/env python3
""" correlation """
import numpy as np


def correlation(C):
    """ Function that calculates a correlation matrix """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2:
        raise ValueError("C must be a 2D square matrix")
    n, d = C.shape
    if n != d:
        raise ValueError("C must be a 2D square matrix")
    if n == 1:
        return np.array([[1.]])
    M = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i, j] = C[i, j] / np.sqrt(abs(C[i, i] * C[j, j]))
    return M
