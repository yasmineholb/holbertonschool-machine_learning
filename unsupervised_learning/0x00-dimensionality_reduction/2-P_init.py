#!/usr/bin/env python3
""" Initialize t-SNE """
import numpy as np

def P_init(X, perplexity):
    """ initializes all variables required 
    to calculate the P affinities in t-SNE"""
    (n, d) = X.shape
    sum_X = np.sum(np.square(X), 1)
    D = np.add(np.add(-2 * np.dot(X, X.T), sum_X).T, sum_X)
    P = np.zeros((n, n))
    beta = np.ones((n, 1))
    logU = np.log(perplexity)
    return D, P, beta, logU
