#!/usr/bin/env python3
""" momentum """
import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """ create momentum """
    op = tf.train.MomentumOptimizer(alpha, beta1)
    tr = op.minimize(loss)
    return tr
