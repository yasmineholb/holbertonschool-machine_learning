#!/usr/bin/env python3
""" initialize """
import numpy as np
kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """ Function that initializes
        variables for a Gaussian Mixture Model """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None, None
    if type(k) is not int or k < 0:
        return None, None, None
    m, clss = kmeans(X, k)
    pi = np.full(shape=k, fill_value=1 / k)
    n, d = X.shape
    id1 = np.identity(d)
    S = np.tile(id1, (k, 1)).reshape((k, d, d))
    return pi, m, S
