#!/usr/bin/env python3
""" Play the Atari game"""
from rl.agents import DQNAgent
import numpy as np
import gym


build_model = __import__('train').build_model
build_agent = __import__('train').build_agent
env = gym.make('Breakout-v0')
height, width, channels = env.observation_space.shape
actions = env.action_space.n
model = build_model(height, width, channels, actions)
agn = build_agent(model, actions)
agn.compile(Adam(lr=1e-4))
agn.load_weights('policy.h5f')
scr = agn.test(env, nb_episodes=10, visualize=True)
