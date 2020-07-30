#!/usr/bin/env python3
""" function"""


class Binomial:
    """class"""
    def __init__(self, data=None, n=1, p=0.5):
        """ function """
        self.data = data
        if data is None:
            self.n = round(float(n))
            self.p = float(p)
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p < 0 and p > 1:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.p = (sum(data)/len(data))/p*0.01
            self.n = round(len(data)/2)
            """self.p = len(data)/self.n"""

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
        if k <= 0:
            return 0
        """t = self.n - k"""
        return (self.p ** k) * ((1 -self.p) ** (1-k))
        """return self.factt(self.n)/(self.factt(p) * self.factt(k))"""
        
