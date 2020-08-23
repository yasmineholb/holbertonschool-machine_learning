#!/usr/bin/env python3
""" RMSProp
"""
import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """ create RMS """
    op = tf.train.RMSPropOptimizer(alpha, beta2, epsilon)
    RM = op.minimize(loss)
    return RM
