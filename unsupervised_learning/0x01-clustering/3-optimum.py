#!/usr/bin/env python3
""" Optimize k """
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """ Function that tests for the optimum number of
        clusters by variance """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None
    if type(kmin) is not int or kmin <= 0:
        return None, None
    if type(kmax) is not int or kmax <= 0:
        return None, None
    if kmin >= X.shape[0] or kmax >= X.shape[0]:
        return None, None
    if kmin >= kmax:
        return None, None
    if type(iterations) is not int or iterations <= 0:
        return None, None
    results = []
    d_vars = []
    c_min, clss1 = kmeans(X, kmin)
    var_min = variance(X, c_min)
    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k)
        results.append((C, clss))
        var = variance(X, C)
        d_vars.append(var_min - var)
    return results, d_vars
