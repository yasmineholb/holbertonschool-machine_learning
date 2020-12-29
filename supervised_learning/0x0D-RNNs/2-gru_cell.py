#!/usr/bin/env python3
""" GRU cell """

import numpy as np


class GRUCell:
    """ Gated recurrent unit """

    def __init__(self, i, h, o):
        """ Constructor """
        self.Wz = np.random.normal(size=(i + h, h))
        self.Wr = np.random.normal(size=(i + h, h))
        self.Wh = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=(h, o))
        self.bz = np.zeros((1, h))
        self.bz = np.zeros((1, h))
        self.br = np.zeros((1, h))
        self.bh = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def softmax(self, x):
        """ Function that calculates softmax """
        return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

    def forward(self, h_prev, x_t):
        """ Function that performs forward
            propagation for one time step """
        hh = np.concatenate((h_prev, x_t), axis=1)
        rt = np.dot(hh, self.Wr) + self.br
        rt = 1 / (1 + np.exp(-rt))
        zt = np.dot(hh, self.Wz) + self.bz
        zt = 1 / (1 + np.exp(-zt))
        hh = np.concatenate(((rt * h_prev).T, x_t.T), axis=0)
        htt = np.tanh((hh.T @ self.Wh) + self.bh)
        h_next = (1 - zt) * h_prev + zt * htt
        y = self.softmax((h_next @ self.Wy) + self.by)
        return h_next, y
