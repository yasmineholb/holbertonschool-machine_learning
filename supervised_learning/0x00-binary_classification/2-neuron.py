#!/usr/bin/env python3
""" new class """
import numpy as np


class Neuron():
    """ class neuron """
    def __init__(self, nx):
        """ init function """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """ getter W """
        return self.__W

    @property
    def b(self):
        """ getter b """
        return self.__b

    @property
    def A(self):
        """ getter A """
        return self.__A

    def forward_prop(self, X):
        """ forward function """
        nx, m = np.shape(X)
        x = np.matmul(self.__W, X) + self.__b
        self.__A = 1/(1 + (np.exp(-x)))
        return self.__A
