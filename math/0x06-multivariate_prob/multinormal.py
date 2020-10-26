#!/usr/bin/env python3
""" Multinormal """
import numpy as np


class MultiNormal:
    """ Class Multinormal """
    def __init__(self, data):
        """ Funtion that represents a Multivariate
            Normal distribution """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")
        d, n = data.shape
        self.mean = np.mean(data, axis=1, keepdims=True)
        xi = data - self.mean
        self.cov = np.matmul(xi, xi.T) / (n - 1)
