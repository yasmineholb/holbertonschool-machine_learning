#!/usr/bin/env python3
""" new class """
import numpy as np
import matplotlib.pyplot as plt


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

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """ gradient descent function """
        m = Y.shape[1]
        p = self.forward_prop(X) - Y
        self.__W = self.__W - (alpha/m) * np.sum((p)*X, axis=1)
        self.__b = self.__b - (alpha/m) * sum(sum(A - Y))

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """ Training """
        nx, m = np.shape(X)
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        if (verbose is True) or (graph is True):
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step < 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        if verbose is True:
            for i in range(0, iterations+step, step):
                p = self.forward_prop(X)-Y
                z = self.forward_prop(X)
                self.__W = self.__W - (alpha/m) * np.sum((p)*X, axis=1)
                self.__b = self.__b - (alpha/m) * sum(sum(self.__A-Y))
                self.__A = self.forward_prop(X)
                print("Cost after {} iterations: {}".
                      format(i, self.cost(Y, z)))
        if graph is True:
            plt.ylabel('cost')
            plt.xlabel('iteration')
            plt.title('Training Cost')
            y = np.arange(0, iterations+step, step)
            plt.plot(y)
            plt.ylim(0, 4)
            plt.xlim(0, iterations+step)
            plt.show()
        return np.round(self.__A).astype(np.int), self.cost(Y, self.__A)
