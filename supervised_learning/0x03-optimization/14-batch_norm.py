#!/usr/bin/env python3
""" batch norm
"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """ create batch """
    scope = tf.variable_scope(None, default_name='layer').__enter__()
    kernel = tf.contrib.layers.variance_scaling_initializer(factor=2.0,
                                                            mode="FAN_AVG")
    ds = tf.layers.dense(prev, units=n, activation=activation,
                         kernel_initializer=kernel,
                         name="layer", reuse=tf.AUTO_REUSE)
    """ds = linear_model(prev)"""
    i, j = tf.nn.moments(ds, axes=[0])
    gamma = tf.Variable(tf.constant(1.0, shape=[n]),
                        name="gamma", trainable=True)
    beta = tf.Variable(tf.constant(0.0, shape=[n]),
                       name="beta", trainable=True)
    scope.reuse_variables()
    batch = tf.nn.batch_normalization(ds, mean=i, variance=j,
                                      offset=beta, scale=gamma,
                                      variance_epsilon=1e-8)
    return batch
