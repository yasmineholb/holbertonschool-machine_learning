#!/usr/bin/env python3
""" RNN """

import numpy as np


def rnn(rnn_cell, X, h_0):
    """ Function that performs forward
        propagation for a simple RNN """
    t, m, i = X.shape
    n, h = h_0.shape
    H = np.zeros((t + 1, m, h))
    Y = np.zeros((t, m, rnn_cell.Wy.shape[1]))
    H[0] = h_0
    h1 = h_0
    for j in range(t):
        x1 = X[j]
        h1, y1 = rnn_cell.forward(h1, x1)
        H[j + 1] = h1
        Y[j] = y1
    return H, Y
