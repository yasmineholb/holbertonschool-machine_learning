#!/usr/bin/env python3
""" function def """
import numpy as np


def one_hot_encode(Y, classes):
    """ one hot """
    if Y is None or classes is None:
        return None
    try:
        """b = np.zeros((Y.size, classes))
        b[np.arange(Y.size), Y] = 1
        return b"""
        b = np.zeros((classes, Y.size))
        for i, j in enumerate(Y):
            b[j][i] = 1
        return b
    except Exception:
        return None
