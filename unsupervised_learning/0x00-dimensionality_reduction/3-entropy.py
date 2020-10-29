#!/usr/bin/env python3
""" HP """
import numpy as np


def HP(Di, beta):
    """ Function that calculates the Shannon
        entropy and P affinities relative to a data point """
    P = np.exp(-Di.copy() * beta)
    sumP = sum(P)
    H = np.log2(sumP) + beta * np.sum(Di * P) / sumP
    P = P / sumP
    return H, P
