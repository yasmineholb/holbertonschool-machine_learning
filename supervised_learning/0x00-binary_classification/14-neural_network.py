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
        self.__A1 = 1/(1 + (np.exp(-(x1))))
        x2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1/(1 + (np.exp(-(x2))))
        return self.__A1, self.__A2

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

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """ gradient descent function """
        nx, m = np.shape(X)
        B = np.dot(self.__W2.T, A2 - Y) * A1 * (1 - A1)
        self.__W2 -= (alpha/m) * np.dot(A2-Y, A1.T)
        self.__b2 -= alpha * np.asarray([[np.mean(A2-Y)]])
        self.__W1 -= (alpha/m) * np.dot(B, X.T)
        self.__b1 -= alpha * np.asarray([[np.mean(B)]])

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """ Training """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        nx, m = np.shape(X)
        for i in range(iterations):
            self.__A1, self.__A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha=0.05)
        return self.evaluate(X, Y)
