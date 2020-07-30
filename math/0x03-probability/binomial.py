#!/usr/bin/env python3
""" function"""


class Binomial:
    """class"""
    def __init__(self, data=None, n=1, p=0.5):
        """ function """
        self.data = data
        if data is None:
            self.n = int(n)
            self.p = float(p)
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data)/len(data)
            var = [(i - mean)**2 for i in data]
            cat = sum(var)/len(data)
            self.p = 1 - (cat/mean)
            self.n = int(round(mean/self.p))
            self.p = mean/self.n

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
        if k < 0:
            return 0
        return (self.p ** k) * ((1 - self.p) ** (1 - k))

    def cal(self, k):
        """ cal function """
        t = self.n - k
        return self.factt(self.n)/(self.factt(t) * self.factt(k))

    def cdf(self, k):
        """ cdf function """
        k = int(k)
        if k < 0:
            return 0
        for i in range(k+1):
            return self.pmf(k) * self.cal(k)
