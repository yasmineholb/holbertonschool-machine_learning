#!/usr/bin/env python3
""" new class """
import numpy as np


class NeuralNetwork():
    """ neural network class"""
    def __init__(self, nx, nodes):
        """ init function """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros(shape=(nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """ self fn """
        return self.__W1

    @property
    def b1(self):
        """ self fn """
        return self.__b1

    @property
    def A1(self):
        """ self fn """
        return self.__A1

    @property
    def W2(self):
        """ self fn """
        return self.__W2

    @property
    def b2(self):
        """ self fn """
        return self.__b2

    @property
    def A2(self):
        """ self fn """
        return self.__A2

    def forward_prop(self, X):
        """ forward function """
        nx, m = np.shape(X)
        x1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = 1/(1 + (np.exp(-x1)))
        x2 = nx * X + self.__b2
        self.__A2 = 1/(1 + (np.exp(-x2)))
        return self.__A1, self.__A2
