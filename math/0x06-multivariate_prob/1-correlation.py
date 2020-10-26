#!/usr/bin/env python3
""" correlation """
import numpy as np


def correlation(C):
    """ Function that calculates a correlation matrix """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
<<<<<<< HEAD
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
=======
    n, d = C.shape
    if n != d or len(C.shape) != 2:
>>>>>>> ff099df0343f833fd0f44239abcb491717455aaf
        raise ValueError("C must be a 2D square matrix")
    d = np.diag(C)
    ch = d.reshape(-1, 1)
    Sqrt = np.sqrt(ch)
    SD = np.matmul(Sqrt, Sqrt.T)
    corr = C / SD
    return corr
