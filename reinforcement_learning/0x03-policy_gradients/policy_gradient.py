#!/usr/bin/env python3
""" Simple Policy function """
import numpy as np


def policy(matrix, weights):
    """ Function that computes to policy with a weight of a matrix"""
    z = matrix.dot(weights)
    exp = np.exp(z)
    return exp / np.sum(exp)

	
def policy_gradient(state, weight):
    """ Function that implements a full training """
    P = policy(state, weight)
    action = np.random.choice(len(P[0]), p=P[0])
    s = P.reshape(-1, 1)
    softmax = np.diagflat(s) - np.dot(s, s.T)
    dsoftmax = softmax[action, :]
    dlog = dsoftmax / P[0, action]
    grad = state.T.dot(dlog[None, :])
    return action, grad