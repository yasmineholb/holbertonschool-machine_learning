#!/usr/bin/env python3
""" new class """
import numpy as np


class DeepNeuralNetwork():
    """ DeepNeuralNetwork class"""
    def __init__(self, nx, layers):
        """ init function """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or layers == []:
            raise TypeError("layers must be a list of positive integers")
        for i in layers:
            if (type(i) is not int) or (i <= 0):
                raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(1, self.L):
            self.weights["b" + str(i + 1)] = np.zeros((layers[i], 1))
            self.weights["W" + str(i + 1)] = np.random.randn(
                layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])
        self.weights["W1"] = np.random.randn(layers[0], nx) * np.sqrt(2 / nx)
        self.weights["b1"] = np.zeros((layers[0], 1))

    @property
    def L(self):
        """ self fn """
        return self.__L

    @property
    def cache(self):
        """ self fn """
        return self.__cache

    @property
    def weights(self):
        """ self fn """
        return self.__weights
