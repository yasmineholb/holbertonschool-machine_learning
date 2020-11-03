#!/usr/bin/env python3
""" Initialize K-means """
import numpy as np


def initialize(X, k):
    """ Function that initializes cluster
        centroids for K-means """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None
    if k < 0 or type(k) is not int:
        return None
    mx = np.max(X, axis=0)
    mn = np.min(X, axis=0)
    n, d = X.shape
    centroids = np.random.uniform(low=mn, high=mx, size=(k, d))
    return centroids
