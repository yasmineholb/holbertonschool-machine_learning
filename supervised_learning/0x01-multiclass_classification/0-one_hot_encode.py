#!/usr/bin/env python3
""" function def """
import numpy as np


def one_hot_encode(Y, classes):
    """ one hot """
    b = np.zeros((Y.size, classes+1))
    b[np.arange(Y.size), Y] = 1
    return b
