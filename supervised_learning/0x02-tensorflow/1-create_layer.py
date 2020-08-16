#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def create_layer(prev, n, activation):
    """ create layer function """
    scope = tf.variable_scope(None, default_name='layer').__enter__()
    kernel = tf.contrib.layers.variance_scaling_initializer(factor=2.0,
                                                            mode="FAN_AVG")
    linear_model = tf.layers.dense(prev, units=n, activation=activation,
                                   kernel_initializer=kernel,
                                   name="layer", reuse=tf.AUTO_REUSE)
    scope.reuse_variables()
    return(linear_model)
