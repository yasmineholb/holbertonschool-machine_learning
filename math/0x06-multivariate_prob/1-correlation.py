#!/usr/bin/env python3
""" correlation """
import numpy as np


def correlation(C):
    """ Function that calculates a correlation matrix """
    if not isinstance(C, np.ndarray) or len(C.shape) != 2:
        raise TypeError("C must be a 2D numpy.ndarray")
    if C.shape[0] < 2:
        raise ValueError("C must contain multiple data points")
    n, d = C.shape
    if n != d:
        raise ValueError('C must be a 2D square matrix')
    M = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i, j] = C[i, j] / np.sqrt(abs(C[i, i] * C[j, j]))
    return M
