#!/usr/bin/env python3
""" Bidirectional Cell Forward """

import numpy as np


class BidirectionalCell():
    """ Function that  that represents
        a bidirectional cell of an RNN """

    def __init__(self, i, h, o):
        """ Constructor """
        self.Whf = np.random.normal(size=(i + h, h))
        self.Whb = np.random.normal(size=(i + h, h))
        self.Wy = np.random.normal(size=((2 * h), o))
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """ Functin that calculates the hidden state
            in the forward direction for one time step """
        hh = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.dot(hh, self.Whf) + self.bhf)
        return h_next

    def backward(self, h_next, x_t):
        """ Function that calculates the hidden state
            in the backward direction for one time step"""
        hh = np.concatenate((h_next, x_t), axis=1)
        h_prev = np.tanh(np.dot(hh, self.Whb) + self.bhb)
        return h_prev

    def output(self, H):
        """ Function that calculates all outputs for the RNN """
        t, m, h = H.shape
        o1 = self.by.shape[1]
        Y = np.zeros((t, m, o1))
        for i in range(t):
            y1 = np.dot(H[i], self.Wy) + self.by
            y1 = np.exp(y1) / np.sum(np.exp(y1), axis=1,
                                     keepdims=True)
            Y[i] = y1
        return Y
