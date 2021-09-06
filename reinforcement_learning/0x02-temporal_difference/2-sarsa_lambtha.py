#!/usr/bin/env python3
""" SARSA(lambtha) """

import numpy as np
import gym


def epsilon_greedy(env, Q, state, epsilon):
    """ Function that calculates epsilon """
    action = 0
    if np.random.uniform(0, 1) < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state, :])
    return action


def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100,
                  alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1,
                  epsilon_decay=0.05):
    """ Function that performs SARSA(lambtha) """
    init_epsilon = epsilon
    Et = np.zeros((Q.shape))
    for i in range(episodes):
        state = env.reset()
        action = epsilon_greedy(env, Q, state, epsilon)
        for j in range(max_steps):
            Et = Et * lambtha * gamma
            Et[state, action] += 1.0
            new_state, reward, done, info = env.step(action)
            new_action = epsilon_greedy(env, Q, state, epsilon)
            delta_t = reward + gamma + Q[new_state, new_action] - Q[state,
                                                                    action]
            Q[state, action] = Q[state, action] + alpha * delta_t * Et[state,
                                                                       action]
            if done:
                break
            state = new_state
            action = new_action
        epsilon = (min_epsilon + (init_epsilon - min_epsilon)
                   * np.exp(- epsilon_decay * i))
    return Q
