#!/usr/bin/env python3
""" shuffle_data """
import numpy as np


def shuffle_data(X, Y):
    """ shuffle_data function """
    x = X.copy()
    y = Y.copy()
    np.random.shuffle(x)
    np.random.shuffle(y)
    return x, y
