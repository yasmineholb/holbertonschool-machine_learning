#!/usr/bin/env python3
""" correlation """
import numpy as np


def correlation(C):
    """ Function that calculates a correlation matrix """
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
