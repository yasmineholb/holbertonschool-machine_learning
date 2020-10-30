#!/usr/bin/env python3
""" marginal """
import numpy as np


def marginal(x, n, P, Pr):
    """ Function that calculates the marginal probability
        of obtaining the data """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        error = "x must be an integer that is greater than or equal to 0"
        raise ValueError(error)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    for j in P:
        if j < 0 or j > 1:
            raise ValueError("All values in P must be in the range [0, 1]")
    for j in Pr:
        if j < 0 or j > 1:
            raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    f = np.math.factorial
    fact = f(n) / (f(x) * f(n-x))
    puiss = (P ** x) * ((1 - P) ** (n - x))
    intt = fact * puiss * Pr
    return sum(intt)
