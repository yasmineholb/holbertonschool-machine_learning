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
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(self.__L):
            if (type(layers[i]) is not int) or (layers[i] <= 0):
                raise TypeError("layers must be a list of positive integers")
            if i > 0:
                self.weights["b" + str(i + 1)] = np.zeros((layers[i], 1))
                self.weights["W" + str(i + 1)] = np.random.randn(
                    layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])
            else:
                self.weights["W1"] = np.random.randn(layers[0], nx) * np.sqrt(
                    2 / nx)
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

    def forward_prop(self, X):
        """ forward function """
        nx, m = np.shape(X)
        self.__cache["A0"] = X
        for i in range(self.__L):
            s = np.matmul(self.__weights["W" + str(i+1)], self.__cache[
                "A" + str(i)]) + (self.__weights["b" + str(i+1)])
            self.__cache["A" + str(i+1)] = 1/(1 + (np.exp(-(s))))
        return self.__cache["A" + str(self.__L)], self.__cache

    def cost(self, Y, A):
        """ cost function """
        m = Y.shape[1]
        cos = -(np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)))
        return cos/m

    def evaluate(self, X, Y):
        """ evaluate function """
        z, p = self.forward_prop(X)
        t = np.round(p)
        return t.astype(np.int), self.cost(Y, p)
