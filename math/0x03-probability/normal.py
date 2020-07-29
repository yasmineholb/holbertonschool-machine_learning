#!/usr/bin/env python3
""" function"""


class Normal:
    """ Normal """
    def __init__(self, data=None, mean=0., stddev=1.):
        """ function """
        self.data = data
        """self.lambtha = float(lambtha)"""
        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data)/len(data)
            dt = [(i - self.mean)**2 for i in data]
            self.stddev = (sum(dt)/(len(data)))**(0.5)

    def z_score(self, x):
        """ z_score function """
        return (x - self.mean)/self.stddev

    def x_value(self, z):
        """ x-value function """
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """ pdf function """
        p = (self.z_score(x)) ** 2
        pi = 3.1415926536
        e = 2.7182818285
        return (1 / (self.stddev * ((2 * pi)**0.5)) * (e ** ((-0.5) * p)))
