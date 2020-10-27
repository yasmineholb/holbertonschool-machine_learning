""" pca """
import numpy as np


def pca(X, ndim):
    """ Function that performs PCA on a dataset: """
    W = np.linalg.svd(X)[2][:ndim, :].T
    return np.matmul(X, W)
