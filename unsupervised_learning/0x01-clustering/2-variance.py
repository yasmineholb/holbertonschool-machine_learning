#!/usr/bin/env python3
""" Variance """
import numpy as np


def variance(X, C):
    """ Function that calculates the total
        intra-cluster variance for a data set """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None
    if type(C) is not np.ndarray or len(C.shape) != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None
    n, d = X.shape
    k, d1 = C.shape
    size = C[:, np.newaxis]
    dist = np.linalg.norm((X - size), axis=2)
    min_d = np.min(dist, axis=0)
    variance = np.sum(np.square(min_d))
    return variance
