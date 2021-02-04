#!/usr/bin/env python3
""" maximization """

import numpy as np


def maximization(X, g):
    """ Function that calculates the maximization
        step in the EM algorithm for a GMM"""
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return (None, None, None)
    if type(g) is not np.ndarray or len(g.shape) != 2:
        return (None, None, None)
    if X.shape[0] != g.shape[1]:
        return (None, None, None)
    summ = np.sum(g, axis=0)
    summ = np.sum(summ)
    if (int(summ) != X.shape[0]):
        return (None, None, None)
    n, d = X.shape
    k, t = g.shape
    soft = np.sum(g, axis=1)
    pi = soft / n
    mean = np.zeros((k, d))
    S = np.zeros((k, d, d))
    for clus in range(k):
        rik = g[clus]
        denomin = soft[clus]
        mean[clus] = np.matmul(rik, X) / denomin
        first = rik * (X - mean[clus]).T
        S[clus] = np.matmul(first, (X - mean[clus])) / denomin
    return pi, mean, S
