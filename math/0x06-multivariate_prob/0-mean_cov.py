#!/usr/bin/env python3
""" mean_cov """
import numpy as np


def mean_cov(X):
    """ Function that calculates the mean
        and covariance of a data set """
    n, d = X.shape
    if not isinstance(X, np.ndarray):
        raise TypeError("X must be a 2D numpy.ndarray")
    if n < 2:
        raise ValueError("X must contain multiple data points")
    mean = np.mean(X, axis=0)
    xi = X - mean
    cov = np.matmul(xi.T, xi) / (n - 1)
    return mean, cov
