#!/usr/bin/env python3
""" function"""


class Poisson:
    """class"""
    def __init__(self, data=None, lambtha=1.):
        """ function """
        self.data = data
        """self.lambtha = float(lambtha)"""
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data)/len(data))

    def factt(self, k):
        """ factorial function """
        f = 1
        if k == 0:
            return 1
        for i in range(1, k+1):
            f = f * i
        return f

    def pmf(self, k):
        """ pmf function """
        k = int(k)
        if k < self.lambtha:
            return(0)
        p = ((2.7182818285**(-self.lambtha))*(self.lambtha**k))/self.factt(k)
        return(float(p))

    def cdf(self, k):
        """ cdf function """
        t = self.lambtha
        k = int(k)
        p = 0
        if k < self.lambtha:
            return(0)
        for i in range(k + 1):
            p = p + ((2.7182818285**(-t))*(t**i))/self.factt(i)
        return(p)
