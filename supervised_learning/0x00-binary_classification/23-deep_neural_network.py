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
        t = np.round(z)
        return t.astype(np.int), self.cost(Y, z)

    def gradient_descent(self, Y, cache, alpha=0.05):
        """ gradient descent function  """
        m = np.shape(Y)[1]
        n = self.__L
        ancien = self.__weights["W" + str(n)]
        self.__weights["W" + str(n)] -= alpha/m * np.dot(self.__cache[
            "A" + str(n - 1)], (self.__cache["A" + str(n)] - Y).T).T
        self.__weights["b" + str(n)] -= alpha/m * np.sum(self.__cache[
            "A" + str(n)] - Y, axis=1)
        B = self.__cache["A" + str(n)] - Y
        for i in range(self.__L - 1, 0, -1):
            B = np.dot(ancien.T, B) * self.__cache[
                "A" + str(i)] * (1 - self.__cache["A" + str(i)])
            ancien = self.__weights["W" + str(i)].copy()
            self.__weights["W" + str(i)] -= alpha/m * np.dot(self.__cache[
                "A" + str(i - 1)], B.T).T
            self.__weights["b" + str(i)] -= alpha/m * np.sum(
                B, axis=1, keepdims=True)

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
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
        nx, m = np.shape(X)
        S = []
        Iter = []
        for i in range(iterations+1):
            self.forward_prop(X)
            self.gradient_descent(Y, self.__cache, alpha=0.05)
            s = self.cost(Y, self.__cache["A" + str(self.__L)])
            if verbose is True:
                if (i % step == 0) or (i == iterations):
                    print("Cost after {} iterations: {}".format(i, s))
                    S.append(s)
                    Iter.append(i)
        if graph is True:
            plt.plot(Iter, S, 'b')
            plt.title('Training Cost')
            plt.xlabel('iteration')
            plt.ylabel('Cost')
            plt.show()
        return self.evaluate(X, Y)
