#!/usr/bin/env python3
""" function"""


class Exponential:
    """ Exponential """
    def __init__(self, data=None, lambtha=1.):
        """ fn """
        self.data = data
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(len(data)/sum(data))

    def pdf(self, x):
        """ pdf """
        if x < 0:
            return 0
        p = self.lambtha * (2.7182818285**(-self.lambtha * x))
        if x >= 0:
            return p

    def cdf(self, x):
        """cdf"""
        if x < 0:
            return(0)
        p = 1 - (2.7182818285**(-self.lambtha * x))
        if x >= 0:
            return(p)
