#!/usr/bin/env python3
""" Adam op
"""
import tensorflow as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """ adam op """
    op = tf.train.AdamOptimizer(alpha, beta1, beta2, epsilon)
    ad = op.minimize(loss)
