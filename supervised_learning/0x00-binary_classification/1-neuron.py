#!/usr/bin/env python3
""" new class """
import numpy as np


class Neuron():
    """ neuron class"""
    def __init__(self, nx):
        """ init function """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise TypeError("nx must be a positive integer")
        self.__W = np.random.randn(nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """ self fn """
        return self.__W

    @property
    def b(self):
        """ self fn """
        return self.__b

    @property
    def A(self):
        """ self fn """
        return self.__A
