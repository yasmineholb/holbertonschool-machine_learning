#!/usr/bin/env python3
""" mean_cov """
import numpy as np


def mean_cov(X):
    """ Function that calculates the mean
        and covariance of a data set """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")
    n, d = X.shape
    mean = np.mean(X, axis=0, keepdims=True)
    xi = X - mean
    cov = np.matmul(xi.T, xi) / (n - 1)
    return mean, cov
