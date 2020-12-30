#!/usr/bin/env python3
""" Bidirectional RNN  """

import numpy as np


def bi_rnn(bi_cell, X, h_0, h_t):
    """ Function that performs forward
        propagation for a bidirectional RNN """
    m, h = h_0.shape
    t, m, i = X.shape
    h_f = np.zeros((t, m, h))
    h_b = np.zeros((t, m, h))
    h1 = h_0
    h2 = h_t
    for i in range(t):
        x1 = X[i]
        x2 = X[-(i + 1)]
        h1 = bi_cell.forward(h1, x1)
        h2 = bi_cell.backward(h2, x2)
        h_f[i] = h1
        h_b[-(i + 1)] = h2
    H = np.concatenate((h_f, h_b), axis=-1)
    Y = bi_cell.output(H)
    return H, Y
