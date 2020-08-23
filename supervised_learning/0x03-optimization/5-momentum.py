#!/usr/bin/env python3
""" Momentum Grad
Ref. Les clients ayant consulté Hands-On Machine Learning
with Scikit-Learn and TensorFlow
"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """Momentum Grad"""
    v = beta1 * v + alpha * grad
    var = var - v
    return var, v
