#!/usr/bin/env python3
""" l2 regularization function """
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """ function that updates the weights and biases of a neural
        network using gradient descent with L2 regularization """
    d_z = cache["A" + str(L)] - Y
    m = len(Y[0])
    for i in range(L, 0, -1):
        Actv = cache["A" + str(i - 1)]
        d_w = (1 / m) * np.matmul(d_z, Actv.T)
        d_b = (1 / m) * np.sum(d_z, axis=1, keepdims=True)
        b = "b" + str(i)
        w = "W" + str(i)
        d = "D" + str(i-1)
        if i != 1:
            d_A = np.dot(weights[w].T, d_z)
            d_A = np.multiply(cache[d], d_A)
            d_A = d_A / keep_prob
            d_z = (1-(Actv**2)) * d_A
        weights[b] = weights[b] - alpha * d_b
        weights[w] = weights[w] - alpha * d_w
