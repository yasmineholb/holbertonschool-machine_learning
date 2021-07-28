#!/usr/bin/env python3
""" Initialize Q-table """
import numpy as np
import gym


def q_init(env):
    """Function that initializes the Q-table"""
    q_tab = np.zeros((env.observation_space.n, env.action_space.n))
    return q_tab
