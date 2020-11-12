#!/usr/bin/env python3
""" Absorbing """
import numpy as np


def absorbing(P):
    """function that determines if a markov chain is absorbing"""
    if type(P) is not np.ndarray or len(P.shape) != 2:
        return None
    e = np.diag(P)
    n = len(P)
    if np.max(e) != 1:
        return False
    elif (P == np.eye(n)).all():
        return True
    else:
        u = np.where(e == 1)
        j = 0
        for i in u[0]:
            S = np.eye(n)
            S[i, i] = 0
            S[n - j - 1, n - j - 1] = 0
            S[i, n - j - 1] = 1
            S[n - j - 1, i] = 1
            P = np.dot(S, np.dot(P, S))
            j += 1
        Q = P[0:n - j, 0:n - j]
        R = P[0:n - j, n - j:n]
        QI = np.eye(n - j) - Q
        if np.linalg.det(QI) == 0:
            return False
        else:
            return True
