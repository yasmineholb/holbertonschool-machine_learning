#!/usr/bin/env python3
""" RMSProp
"""
import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """ create RMS """
    op = tf.train.RMSPropOptimizer(learning_rate=alpha, decay=beta2,
                                   epsilon=epsilon)
    RM = op.minimize(loss)
    return RM
