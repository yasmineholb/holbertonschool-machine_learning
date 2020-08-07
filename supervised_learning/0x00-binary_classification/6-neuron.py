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

    def cost(self, Y, A):
        """ cost function """
        m = Y.shape[1]
        cos = -(np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)))
        return cos/m

    def evaluate(self, X, Y):
        """ evaluate function """
        z = self.forward_prop(X)
        s = np.round(z)
        return s.astype(np.int), self.cost(Y, z)

    """def gradient_descent(self, X, Y, A, alpha=0.05):
        gradient descent function 
        m = Y.shape[1]
        p = self.forward_prop(X) - Y
        self.__W = self.__W - (alpha/m) * np.sum((p)*X, axis=1)
        self.__b = self.__b - (alpha/m) * sum(sum(A - Y))

    def train(self, X, Y, iterations=5000, alpha=0.05):
        Training 
        nx, m = np.shape(X)
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        for i in range(iterations):
            p = self.forward_prop(X)-Y
            self.__W = self.__W - (alpha/m) * np.sum((p)*X, axis=1)
            self.__b = self.__b - (alpha/m) * sum(sum(self.__A-Y))
            self.__A = self.forward_prop(X)
        return np.round(self.__A).astype(np.int), self.cost(Y, self.__A)
        for i in range(iterations):
            self.__W, self.__b = self.gradient_descent(X, Y, self.__A, alpha=0.05)
            self.__A = self.forward_prop(X)
        return np.round(self.__A).astype(np.int), self.cost(Y, self.__A)"""
    def gradient_descent(self, X, Y, A, alpha=0.05):
        """ gradient descent function """
        nx, m = np.shape(X)
        self.__W = self.__W - (alpha/m) * np.matmul(X, (A-Y).T).T
        self.__b = self.__b - (alpha/m) * np.sum(A-Y).T
        return self.__W, self.__b
    
    def train(self, X, Y, iterations=5000, alpha=0.05):
        """ Training """
        nx, m = np.shape(X)
        for i in range(iterations):
            self.__W, self.__b = self.gradient_descent(X, Y, self.__A, alpha=0.05)
            self.__A = self.forward_prop(X)
        return np.round(self.__A).astype(np.int), self.cost(Y, self.__A)
