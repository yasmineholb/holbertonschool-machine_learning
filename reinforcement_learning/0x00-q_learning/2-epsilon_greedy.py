#!/usr/bin/env python3
""" Epsilon Greedy """
import numpy as np
import gym


def epsilon_greedy(Q, state, epsilon):
    """Function that uses epsilon-greedy
    to determine the next action"""
    p = np.random.uniform(0, 1)
    if p > epsilon:
        action = np.argmax(Q[state, :])
    else:
        action = np.random.randint(0, Q.shape[1])
    return action
