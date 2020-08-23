#!/usr/bin/env python3
""" Adam
Ref. Hands-On Machine Learning
with Scikit-Learn and TensorFlow
"""
import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """ update fn """
    v1 = beta1 * v + (1 - beta1) * grad
    s1 = beta2 * s + (1 - beta2) * grad ** 2
    v2 = (1 / (1 - (beta1 ** t))) * v1
    s2 = (1 / (1 - (beta2 ** t))) * s1
    var = var - (alpha * (v2 / (np.sqrt(s2) + epsilon)))
    return var, v1, s1
