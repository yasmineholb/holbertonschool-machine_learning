#!/usr/bin/env python3
""" shuffle_data """
import numpy as np


def shuffle_data(X, Y):
    """ shuffle_data function """
    n, m = np.shape(X)
    x = np.concatenate((X, Y), axis=1)
    np.random.shuffle(x)
    x_shuffled = x[:, 0:m]
    y_shuffled = x[:, m:]
    return x_shuffled, y_shuffled
