#!/usr/bin/env python3
""" shuffle_data """
import numpy as np


def shuffle_data(X, Y):
    """ shuffle_data function """
    n, m = np.shape(X)
    x = np.concatenate((X, np.linspace(0, n-1, n).reshape(n, 1)), axis=1)
    np.random.shuffle(x)
    x_shuffled = x[:, 0:-1]
    permutation = x[:, m].astype(np.int)
    y_shuffled = np.zeros(np.shape(Y))
    for i in range(n):
        y_shuffled[i, :] = Y[permutation[i], :]
    return x_shuffled, y_shuffled
