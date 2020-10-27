#!/usr/bin/env python3
""" pca """
import numpy as np


def pca(X, var=0.95):
    """ Function that performs PCA on a dataset: """
    tab = np.matmul(X.T, X)
    V = np.linalg.eig(tab)[0]
    V = abs(V)
    V = np.sqrt(V)
    V = V / sum(V)
    la = []
    S = 0
    while S < var:
        S += V[np.argmax(V)]
        la.append(np.argmax(V))
        V[np.argmax(V)] = -1
    return np.linalg.eig(tab)[1][:, la]
