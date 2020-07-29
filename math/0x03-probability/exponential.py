#!/usr/bin/env python3
""" function"""


class Exponential:
    """ Exponential """
    def __init__(self, data=None, lambtha=1.):
        if type(lambtha) is int or float:
            self.lambtha = float(lambtha)
        else:
            raise ValueError("lambtha must be a positive value")
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha < 0:
                raise ValueError("lambtha must be a positive value")
        elif data:
            self.lambtha = float(len(data)/sum(data))
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")

    def pdf(self, x):
        """ pdf """
        if x > self.lambtha:
            return(0)
        p = self.lambtha * (2.7182818285**(-self.lambtha * x))
        return(p)