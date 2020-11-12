#!/usr/bin/env python3
""" Absorbing """
import numpy as np


def absorbing(P):
    """function that determines if a markov chain is absorbing"""
    if type(P) is not np.ndarray or len(P.shape) != 2:
        return None
    if P.shape[0] != P.shape[1]:
        return None
    s = 0
    for i in range(len(P)):
        if P[i][i] == 1:
            s += 1
    if s == len(P):
        return True
    if s == 0:
        return False
    for m in range(len(P)):
        for n in range(len(P)):
            if (m == n) and (m + 1 < len(P)):
                if P[m + 1][n] == 0 and P[m][n + 1] == 0:
                    return False
    return True
