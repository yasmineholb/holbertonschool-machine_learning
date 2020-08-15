#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def create_layer(prev, n, activation):
    """ create layer function """
    kernel = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    linear_model = tf.layers.dense(prev, units=n, activation=activation,
                                   use_bias=True,
                                   kernel_initializer=kernel,
                                   name="layer")
    return(linear_model)
