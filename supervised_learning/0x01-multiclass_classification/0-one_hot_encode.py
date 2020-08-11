#!/usr/bin/env python3
""" function def """
import numpy as np


def one_hot_encode(Y, classes):
    """ one hot """
    if Y is None or classes is None:
        return None
    if len(Y) == 0:
        return None
    if classes < 0:
        return None
    if type(classes) is not int:
        return None
    try:
        b = np.zeros((Y.size, classes))
        b[np.arange(Y.size), Y] = 1
        return b
    except Exception:
        return None
