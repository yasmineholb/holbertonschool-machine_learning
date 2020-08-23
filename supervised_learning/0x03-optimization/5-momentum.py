#!/usr/bin/env python3
""" Momentum Grad
Ref.  Hands-On Machine Learning
with Scikit-Learn and TensorFlow
"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """Momentum Grad Better than asked for
    v = beta1 * v + alpha * grad
    var = var - v
    return var, v """
    v = beta1 * v + (1 - beta1) * grad
    var = var - alpha * v
    return var, v
