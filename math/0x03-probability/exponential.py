#!/usr/bin/env python3
""" function"""


class Exponential:
    """ Exponential """
    def __init__(self, data=None, lambtha=1.):
        self.lambtha = float(lambtha)
        if data is None:
            data = self.lambtha
            if lambtha < 0:
                raise ValueError("lambtha must be a positive value")
        elif data:
            self.lambtha = float(100/sum(data))
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
