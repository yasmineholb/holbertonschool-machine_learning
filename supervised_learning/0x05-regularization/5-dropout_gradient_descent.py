#!/usr/bin/env python3
""" l2 regularization function """
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """ function that updates the weights of a neural network
    with Dropout regularization using gradient descent"""
    copy_w = weights.copy()
    d_z = cache["A" + str(L)] - Y
    m = len(Y[0])
    for i in range(L, 0, -1):
        b = "b" + str(i)
        w = "W" + str(i)
        d = "D" + str(i - 1)
        Actv = cache["A" + str(i - 1)]
        d_b = (1 / m) * np.sum(d_z, axis=1, keepdims=True)
        d_w = (1 / m) * np.matmul(d_z, Actv.T)
        weights[w] = weights[w] - alpha * d_w
        weights[b] = weights[b] - alpha * d_b
        da = 1 - Actv * Actv
        if i > 1:
            d_z = np.matmul(copy_w[w].T, d_z) * da * cache[d] / keep_prob
        else:
            d_z = np.matmul(copy_w[w].T, d_z) * da
