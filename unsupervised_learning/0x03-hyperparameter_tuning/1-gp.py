#!/usr/bin/env python3
""" Initialize Gaussian Process """

import numpy as np


class GaussianProcess():
    """ Class that represents a noiseless 1D Gaussian process """
    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """ Function that calculates the covariance
            kernel matrix between two matrices """
        summ = np.sum(X1 ** 2, 1).reshape(-1, 1) + np.sum(X2 ** 2, 1)
        dt = summ + (-2 * np.dot(X1, X2.T))
        res = self.sigma_f ** 2 * np.exp(-0.5 / self.l ** 2 * dt)
        return res

    def predict(self, X_s):
        """ Function that that predicts the mean and
            standard deviation of points in a Gaussian process """
        Kern = self.kernel(self.X, X_s)
        Kern_s = self.kernel(X_s, X_s)
        Kerninv = np.linalg.inv(self.K)
        mul = Kern.T.dot(Kerninv).dot(self.Y)
        mul = np.reshape(mul, -1)
        cov = Kern_s - Kern.T.dot(Kerninv).dot(Kern)
        cov = cov.diagonal()
        return mul, cov
