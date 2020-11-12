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
            while(P[n - 1 - j, n - 1 - j] == 1):
                j += 1
            if i < n - j - 1:
                P[[i, n - j - 1], :] = P[[n - j - 1, i], :]
                P[:, [i, n - j - 1]] = P[:, [n - j - 1, i]]
                j += 1
        j = len(u[0])
        Q = P[0:n - j, 0:n - j]
        R = P[0:n - j, n - j:n]
        QI = np.eye(n - j) - Q
        if np.linalg.det(QI) == 0:
            return False
        else:
            B = np.matmul(np.linalg.inv(QI), R)
            test = 0
            for i in range(j):
                if (B[:, i] == 0).any():
                    test += 1
            if test == j:
                return False
            return True
        
