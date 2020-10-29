#!/usr/bin/env python3
""" Entropy """
import numpy as np


def HP(Di, beta):
    """function that calculates the Shannon entropy3
    and P affinities relative to a data point"""
    Pi = np.exp(- Di * beta)
    Pi /= np.sum(Pi)
    Hi = - np.sum(Pi * np.log2(Pi))
    return Hi, Pi
