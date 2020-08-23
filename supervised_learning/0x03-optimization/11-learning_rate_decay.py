#!/usr/bin/env python3
""" Decay Stepwise
Ref. https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/
inverse_time_decay
"""
import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    alpha = alpha / (1 + (decay_rate * np.floor(global_step / decay_step)))
    return alpha
