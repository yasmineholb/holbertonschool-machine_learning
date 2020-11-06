#!/usr/bin/env python3
""" pdf """
import numpy as np


def pdf(X, m, S):
    """ Function that calculates the probability
        density function of a Gaussian distribution """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None
    if type(m) is not np.ndarray or len(m.shape) != 1:
        return None
    if type(S) is not np.ndarray or len(S.shape) != 2:
        return None
    if X.shape[1] != m.shape[0] or X.shape[1] != S.shape[0]:
        return None
    if S.shape[1] != S.shape[0]:
        return None
    n, d = X.shape
    K = (1 / (((2 * np.pi) ** d) * np.linalg.det(S)) ** (0.5))
    M1 = np.matmul((X - m), np.linalg.inv(S))
    M = -0.5 * np.matmul(M1, (X - m).T).diagonal()
    pdf = K * np.exp(M)
    PDF = np.where(pdf < 1e-300, 1e-300, pdf)
    return PDF
