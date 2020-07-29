#!/usr/bin/env python3
""" function"""


class Poisson:
    """class"""
    def __init__(self, data=None, lambtha=1.):
        """ function """
        self.data = data
        self.lambtha = float(lambtha)
        if data is None:
            data = lambtha
            if lambtha < 0:
                raise ValueError("lambtha must be a positive value")
        elif data:
            self.lambtha = sum(data)/len(data)
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")

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
