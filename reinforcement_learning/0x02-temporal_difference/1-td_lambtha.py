#!/usr/bin/env python3
""" TD(lamdh) """

import numpy as np
import gym


def td_lambtha(env, V, policy, lambtha, episodes=5000,
               max_steps=100, alpha=0.1, gamma=0.99):
    """ Function that performs the TD algorithm """
    episode = [[], []]
    st = [0 for i in range(env.observation_space.n)]
    for i in range(episodes):
        state = env.reset()
        for j in range(max_steps):
            st = list(np.array(st) * lambtha * gamma)
            st[state] += 1
            action = policy(state)
            new_state, reward, done, info = env.step(action)
            delta_t = reward + gamma * V[new_state] - V[state]
            V[state] = V[state] + alpha * delta_t * st[state]
            if done:
                break
            state = new_state
    return np.array(V)
