#!/usr/bin/env python3
""" pca """
import numpy as np


def pca(X, var=0.95):
    """ Function that performs PCA on a dataset: """
    V = np.linalg.svd(X)[1]
    V = V / sum(V)
    S = 0
    nd = 0
    while S < var:
        S += V[nd]
        nd += 1
    W = np.linalg.svd(X, full_matrices=True, compute_uv=True)[2]
    return W[:nd, :].T
