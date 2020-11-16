#!/usr/bin/env python3
""" viterbi """
import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
    """ Function that calculates the most likely sequence
        of hidden states for a hidden markov model """
