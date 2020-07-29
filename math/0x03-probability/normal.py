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
