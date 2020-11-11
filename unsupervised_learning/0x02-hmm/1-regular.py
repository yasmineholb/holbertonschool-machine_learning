#!/usr/bin/env python3
""" markov_chain """
import numpy as np


def regular(P):
    """ determines the steady state
    probabilities of a regular markov chain """
    if type(P) is not np.ndarray or len(P.shape) != 2:
        return None
    VP = np.linalg.eig(np.transpose(P))
    s = np.argmax(VP[0])
    if np.allclose(VP[0][s], 1):
        b = np.sort(VP[0])
        if np.allclose(b[-1], b[-2]):
            return None
        else:
            a = np.abs(np.transpose(VP[1][:, s]))
            return np.array([a / np.sum(a)])
    else:
        return None
