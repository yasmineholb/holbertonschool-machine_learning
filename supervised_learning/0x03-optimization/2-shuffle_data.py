#!/usr/bin/env python3
""" shuffle_data """
import numpy as np


def shuffle_data(X, Y):
    """ shuffle_data function """
    x = np.random.permutation(X)
    y = np.random.permutation(Y)
    y1 = np.random.permutation(y)
    return x, y1
