#!/usr/bin/env python3
""" markov_chain """
import numpy as np


def markov_chain(P, s, t=1):
    """ Function that determines the probability of a
        markov chain being in a particular state after
        a specified number of iterations """
    for i in range(t):
        s = np.matmul(s, P)
    if s is not None:
        return s
    return None
