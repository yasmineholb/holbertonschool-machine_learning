#!/usr/bin/env python3
""" Initialize Bayesian Optimization """

import numpy as np
from scipy.stats import norm
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """ Class that that performs Bayesian
        optimization on a noiseless 1D Gaussian process """
    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1,
                 sigma_f=1, xsi=0.01, minimize=True):
        """ Constructor """
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        m1, m2 = bounds
        X_s = np.linspace(m1, m2, num=ac_samples)
        self.X_s = (np.sort(X_s)).reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """ Function that performs Bayesian
            optimization on a noiseless 1D Gaussian process """
        mul, cov = self.gp.predict(self.X_s)
        if self.minimize is True:
            val = np.min(self.gp.Y)
            fn = val - mul - self.xsi
        else:
            val = np.max(self.gp.Y)
            fn = mul - val - self.xsi
        sig = np.zeros(cov.shape[0])
        for i in range(cov.shape[0]):
            if cov[i] > 0:
                sig[i] = fn[i] / cov[i]
            else:
                sig[i] = 0
            EI = fn * norm.cdf(sig) + cov * norm.pdf(sig)
        X_next = self.X_s[np.argmax(EI)]
        return X_next, EI

    def optimize(self, iterations=100):
        """ Function that optimizes the black-box function """
        box = []
        for i in range(iterations):
            aq, _ = self.acquisition()
            if aq in box:
                break
            aqf = self.f(aq)
            self.gp.update(aq, aqf)
            box.append(aq)
        if self.minimize is True:
            res = np.argmin(self.gp.Y)
        else:
            res = np.argmax(self.gp.Y)
        self.gp.X = self.gp.X[:-1]
        aq = self.gp.X[res]
        aqf = self.gp.Y[res]
        return aq, aqf
