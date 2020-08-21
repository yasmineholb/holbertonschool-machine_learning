#!/usr/bin/env python3
""" norm constatnts """
import numpy as np


def normalization_constants(X):
    """ nromalize constants """
    m = np.mean(X, axis=0)
    s = np.std(X, axis=0)
    """xn = X/X.max(axis = 0)"""
    return m, s
