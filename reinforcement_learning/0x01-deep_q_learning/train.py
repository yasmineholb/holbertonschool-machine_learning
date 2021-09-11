#!/usr/bin/env python3
""" train Atari game """
from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Convolution2D
from tensorflow.keras.optimizers import Adam
import gym
import random
import numpy as np


env = gym.make('Breakout-v0')
height, width, channels = env.observation_space.shape
actions = env.action_space.n


def building_model(height, width, channels, actions):
    """ Function that builds the model """
    model = Sequential()
    model.add(Convolution2D(32, (8, 8), strides=(4, 4),
              activation='relu', input_shape=(3, height, width, channels)))
    model.add(Convolution2D(64, (4, 4), strides=(2, 2), activation='relu'))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


def building_agent(model, actions):
    """ Function taht builds the model """
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps',
                                  value_max=1., value_min=.1, value_test=.2,
                                  nb_steps=10000)
    memory = SequentialMemory(limit=1000, window_length=3)
    agn = DQNAgent(model=model, memory=memory, policy=policy,
                   enable_dueling_network=True, dueling_type='avg',
                   nb_actions=actions, nb_steps_warmup=1000)
    return agn


model = building_model(height, width, channels, actions)
agn = building_agent(model, actions)
agn.compile(Adam(lr=1e-4))
agn.fit(env, nb_steps=10000, visualize=False, verbose=2)


agn.save_weights('policy.h5', overwrite=True)
