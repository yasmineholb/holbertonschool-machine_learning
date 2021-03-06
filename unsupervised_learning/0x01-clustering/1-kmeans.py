#!/usr/bin/env python3
""" K-means """
import numpy as np


def kmeans(X, k, iterations=1000):
    """ Function that performs K-means on a dataset """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None
    if type(k) is not int or k <= 0:
        return None, None
    if type(iterations) is not int or iterations <= 0:
        return None, None
    mx = np.max(X, axis=0)
    mn = np.min(X, axis=0)
    n, d = X.shape
    C = np.random.uniform(low=mn, high=mx, size=(k, d))
    copy_c = np.copy(C)
    for i in range(iterations):
        C1 = C[:, np.newaxis]
        dist = np.linalg.norm((X - C1), axis=2)
        clss = dist.argmin(axis=0)
        for j in range(k):
            if (X[clss == j].size == 0):
                C[j] = np.random.uniform(low=mn, high=mx, size=(1, d))
            else:
                C[j] = (X[clss == j].mean(axis=0))
        dist = np.linalg.norm((X - C1), axis=2)
        clss = dist.argmin(axis=0)
        if (copy_c == C).all():
            break
        copy_c = np.copy(C)
    return C, clss
