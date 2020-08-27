#!/usr/bin/env python3
""" l2 regularization function """
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """ function that updates the weights and biases of a neural
        network using gradient descent with L2 regularization """
    copy_w = weights.copy()
    d_z = cache["A" + str(L)] - Y
    m = len(Y[0])
    for i in range(L, 0, -1):
        Actv = cache["A" + str(i - 1)]
        d_b = (1 / m) * np.sum(d_z, axis=1, keepdims=True)
        d_w = (1 / m) * np.matmul(d_z, Actv.T)
        b = "b" + str(i)
        w = "W" + str(i)
        dw_reg = d_w + (lambtha / m) * weights[w]
        weights[w] = weights[w] - alpha * dw_reg
        weights[b] = weights[b] - alpha * d_b
        da = Actv * (1 - Actv)
        d_z = np.matmul(copy_w[w].T, d_z) * da
