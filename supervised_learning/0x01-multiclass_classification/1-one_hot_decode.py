#!/usr/bin/env python3
""" function def """
import numpy as np


def one_hot_decode(one_hot):
    """ one hot decode """
    if one_hot is None:
        return None
    if len(one_hot.shape) != 2:
        return None
    return np.argmax(one_hot, axis=0)
