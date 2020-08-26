#!/usr/bin/env python3
""" l2 regularization function """
import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """ function that updates the weights and biases of a neural
        network using gradient descent with L2 regularization """
    
