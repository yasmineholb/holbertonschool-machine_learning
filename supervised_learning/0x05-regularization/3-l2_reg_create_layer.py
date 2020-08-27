#!/usr/bin/env python3
""" l2 regularization function """
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """ function that creates a tensorflow layer that
        includes L2 regularization"""
    kernel = tf.contrib.layers.l2_regularizer(lambtha)
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    linear_model = tf.layers.Dense(units=n, activation=activation,
                                   kernel_initializer=init,
                                   kernel_regularizer=kernel)
    return(linear_model(prev))
