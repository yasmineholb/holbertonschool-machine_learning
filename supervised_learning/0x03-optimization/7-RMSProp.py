#!/usr/bin/env python3
""" RMSProp
Ref. Hands-On Machine Learning
with Scikit-Learn and TensorFlow
"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """ RMSProp """
    s = beta2 * s + (1 - beta2) * grad * grad
    var = var - alpha * grad / np.sqrt(s + epsilon)
    return var, s
