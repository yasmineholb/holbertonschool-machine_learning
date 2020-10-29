#!/usr/bin/env python3
""" Initialize t-SNE """
import numpy as np


def P_init(X, perplexity):
    """ initializes all variables required
    to calculate the P affinities in t-SNE"""
    n, d = np.shape(X)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            D[i, j] = np.linalg.norm(X[i, :] - X[j, :]) ** 2
    D += D.T
    P = np.zeros((n, n))
    betas = np.ones((n, 1))
    H = np.log2(perplexity)
    return D, P, betas, H
