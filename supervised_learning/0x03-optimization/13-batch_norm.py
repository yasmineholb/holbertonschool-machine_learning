#!/usr/bin/env python3
""" Batach Normalization
Ref. Hands-On Machine Learning
with Scikit-Learn and TensorFlow
"""
import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    mu = np.mean(Z, axis=0)
    s = np.mean((Z - mu) ** 2, axis=0)
    z = (Z - mu) / np.sqrt(s + epsilon)
    return gamma * z + beta
