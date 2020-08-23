#!/usr/bin/env python3
""" batch norm
"""
import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """ create batch """
    kernel = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    ds = tf.layers.dense(prev, units=n, activation=activation,
                         kernel_initializer=kernel,
                         name="layer", reuse=tf.AUTO_REUSE)
    """ds = linear_model(prev)"""
    i, j = tf.nn.moments(ds, axes=[0])
    gamma = tf.Variable(tf.constant(1.0, shape=[n]),
                        name="gamma", trainable=True)
    beta = tf.Variable(tf.constant(0.0, shape=[n]),
                       name="beta", trainable=True)
    batch = tf.nn.batch_normalization(ds, mean=i, variance=j,
                                      offset=beta, scale=gamma,
                                      variance_epsilon=1e-8)
    return activation(batch)
