#!/usr/bin/env python3
""" function def """
import numpy as np


def one_hot_decode(one_hot):
    """ one hot decode """
    if len(one_hot.shape) != 2:
        return None
    if type(one_hot) is not np.ndarray:
        return None
    if (one_hot < 0).all():
        return None
    if (one_hot > 1).all():
        return None
    s = np.argmax(one_hot, axis=0)
    return s
