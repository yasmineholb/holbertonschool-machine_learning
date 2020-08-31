#!/usr/bin/env python3
""" One hot """
import numpy as np


def one_hot(labels, classes=None):
    """ Function  that converts a label
        vector into a one-hot matrix """
    b = np.zeros((labels.size, labels.max()+1))
    b[np.arange(labels.size), labels] = 1
    return b
