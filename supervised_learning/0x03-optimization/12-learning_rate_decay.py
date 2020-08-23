#!/usr/bin/env python3
""" learning decay
"""
import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """ learning decay """
    """dc = tf.train.exponential_decay(learning_rate=alpha,
                                    global_step=global_step,
                                    decay_steps=decay_step,
                                    decay_rate=decay_rate, staircase=False)"""
    dc = alpha * decay_step ** (global_step / decay_step)
    return dc
