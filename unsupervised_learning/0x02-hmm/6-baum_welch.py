#!/usr/bin/env python3
""" baum_welch """
import numpy as np


def baum_welch(Observations, Transition, Emission, Initial,
               iterations=1000):
    """ Function that performs the Baum-Welch algorithm
        for a hidden markov model """
