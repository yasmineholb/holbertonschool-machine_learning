#!/usr/bin/env python3
""" likelihood """
import numpy as np


def likelihood(x, n, P):
    """ Function that  calculates the likelihood
        of obtaining this data given various hypothetical
        probabilities of developing severe side effects """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        msg = "x must be an integer that is greater than or equal to 0"
        raise ValueError(msg)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    for j in P:
        if j < 0 or j > 1:
            raise ValueError("All values in P must be in the range [0, 1]")
    f = np.math.factorial
    fact = f(n) / (f(x) * f(n-x))
    puiss = (P ** x) * ((1 - P) ** (n - x))
    return fact * puiss
