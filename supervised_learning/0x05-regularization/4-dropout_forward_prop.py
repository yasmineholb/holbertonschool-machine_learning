#!/usr/bin/env python3
""" dropout function """
import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """ function that conducts forward propagation
        using Dropout """
    nx, m = np.shape(X)
    cache = {}
    cache["A0"] = X
    for i in range(L):
        A = "A" + str(i)
        w = "W" + str(i+1)
        b = "b" + str(i+1)
        d = "D" + str(i+1)
        A1 = "A" + str(i+1)
        s = np.matmul(weights[w], cache[A]) + (weights[b])
        """Act = 1/(1 + (np.exp(-(s))))"""
        if i == L-1:
            ex = np.exp(s)
            act = ex / ex.sum(axis=0, keepdims=True)
            cache[A1] = act
        else:
            Act = np.tanh(s)
            d1 = np.random.rand(Act.shape[0], Act.shape[1])
            d1 = d1 < keep_prob
            cache[d] = np.multiply(d1, 1)
            Act = np.multiply(Act, d1)
            Act = Act/keep_prob
            cache[A1] = Act
    return cache
