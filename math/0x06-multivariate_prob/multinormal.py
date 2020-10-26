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

    def pdf(self, x):
        """ Function that calculates the PDF at a data point """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d, n = x.shape
        if len(x.shape) != 2 or x.shape[0] != d.shape[1] != 1:
            raise ValueError("x must have the shape ({d}, 1)")
        
