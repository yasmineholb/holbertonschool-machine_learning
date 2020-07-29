#!/usr/bin/env python3
""" function"""


class Poisson:
    def __init__(self, data=None, lambtha=1.):
        """ function """
        self.data = data
        self.lambtha = float(lambtha)
        if data is None:
            data = lambtha
            if lambtha < 0:
                raise TypeError("lambtha must be a positive value")
        elif data:
            self.lambtha = sum(data)/len(data)
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise TypeError("data must contain multiple values")
