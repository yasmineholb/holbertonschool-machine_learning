#!/usr/bin/env python3
""" l2 regularization function """
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """ function that calculates the cost of a neural
        network with L2 regularization """
    sum1 = 0
    i = 0
    for k, w in weights.items():
        if k[i] == 'W':
            sum1 += np.linalg.norm(w)
    l2_reg = sum1 * (lambtha / (2 * m)) + cost
    return l2_reg
