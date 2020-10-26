#!/usr/bin/env python3
""" correlation """
import numpy as np


def correlation(C):
    """ Function that calculates a correlation matrix """
<<<<<<< HEAD
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    p, x = C.shape
    if len(C.shape) != 2 or p != x:
        raise ValueError("C must be a 2D square matrix")
    d = np.diag(C)
    ch = d.reshape(-1, 1)
    Sqrt = np.sqrt(ch)
    SD = np.matmul(Sqrt, Sqrt.T)
    corr = C / SD
    return corr
=======
    if not isinstance(C, np.ndarray) or len(C.shape) != 2:
        raise TypeError("C must be a numpy.ndarray")
    n, d = C.shape
    if n != d:
        raise ValueError("C must be a 2D square matrix")
    if n == 1:
        return np.array([[1]])
    M = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i, j] = C[i, j] / np.sqrt(abs(C[i, i] * C[j, j]))
    return M
>>>>>>> 775ddc40cf36da40c2762d3a38b7a074bc5bb8b9
