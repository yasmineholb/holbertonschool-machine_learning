#!/usr/bin/env python3
""" l2 regularization function """
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """ function that creates a tensorflow layer that
        includes L2 regularization"""
    scope = tf.variable_scope(None, default_name='layer').__enter__()
    kernel = tf.contrib.layers.l2_regularizer(lambtha)
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    linear_model = tf.layers.dense(inputs=prev, units=n, activation=activation,
                                   kernel_initializer=init,
                                   kernel_regularizer=kernel,
                                   name="layer", reuse=tf.AUTO_REUSE)
    scope.reuse_variables()
    return(linear_model)
