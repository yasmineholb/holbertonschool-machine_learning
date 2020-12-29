#!/usr/bin/env python3
""" RNN Cell """

import numpy as np


class RNNCell:
    """ Class that represents a cell of a simple RNN """

    def __init__(self, i, h, o):
        """ Constructor """
        self.Wh = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """ Function that performs forward
            propagation for one time step """
        xh = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.dot(xh, self.Wh) + self.bh)
        y = np.dot(h_next, self.Wy) + self.by
        y = np.exp(y) / np.sum(np.exp(y), axis=1, keepdims=True)
        return (h_next, y)
