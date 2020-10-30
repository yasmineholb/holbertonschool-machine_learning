#!/usr/bin/env python3
""" posterior """
import numpy as np


def posterior(x, n, p1, p2):
    """https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.beta.html
    Ross p 147"""
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        error = "x must be an integer that is greater than or equal to 0"
        raise ValueError(error)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if type(p1) is not float or p1 < 0 or p1 > 0:
        raise ValueError("p1 must be a float in the range [0, 1])
    if type(p2) is not float or p2 < 0 or p2 > 0:
        raise ValueError("p2 must be a float in the range [0, 1])
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    cnp = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    g = special.gamma
    g1 = (g(x + 1) * g(n - x + 1)) / g(n + 2)
    ib = special.betainc
    gg = cnp * g * (n + 1)
    return gg * (ib(x + 1, n - x + 1, p2) - ib(x + 1, n - x + 1, p1))
