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
        """ Funtion that clculates the PDF of a Multivariate
            Normal distribution """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if len(x.shape) != 2:
            raise ValueError("x must have the shape ({d}, 1)")
        if x.shape[0] != d or x.shape[1] != 1:
            raise ValueError("x must have the shape ({d}, 1)")
        K = (1 / (((2 * np.pi) ** d) * np.linalg.det(self.cov)) ** (0.5))
        M1 = np.matmul((x - self.mean).T, np.linalg.inv(self.cov))
        M = -0.5 * np.matmul(M1,(x - self.mean))
        return K * np.exp(M)[0, 0]
    
