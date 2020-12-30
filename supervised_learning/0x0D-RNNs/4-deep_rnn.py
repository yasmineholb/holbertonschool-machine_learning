#!/usr/bin/env python3
""" Deep RNN """

import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """ Function that performs forward
        propagation for a deep RNN """
    t, m, i = X.shape
    l, m, h = h_0.shape
    o = rnn_cells[-1].by.shape[1]
    H = np.zeros((t + 1, l, m, h))
    Y = np.zeros((t, m, o))
    H[0] = h_0
    ct = 0
    for i in range(t):
        x1 = X[i]
        ht = np.zeros((l, m, h))
        for j in range(l):
            h1 = H[ct][j]
            h1, pt = rnn_cells[j].forward(h1, x1)
            x1 = h1
            ht[j] = h1
        Y[i] = pt
        H[i + 1] = ht
        ct += 1
    return H, Y
