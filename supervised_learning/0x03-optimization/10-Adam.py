#!/usr/bin/env python3
""" Adam op
"""
import tensorflow as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """ adam op """
    op = tf.train.AdamOptimizer(learning_rate=alpha, beta1=beta1,
                                beta2=beta2, epsilon=epsilon)
    ad = op.minimize(loss)
