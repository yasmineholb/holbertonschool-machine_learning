#!/usr/bin/env python3
""" Dropout function """
import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob):
    """ function that creates a layer of a neural network
        using dropout"""
    dr = tf.layers.Dropout(keep_prob)
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    linear_model = tf.layers.Dense(units=n, activation=activation,
                                   kernel_initializer=init)
    return(dr(linear_model(prev)))
