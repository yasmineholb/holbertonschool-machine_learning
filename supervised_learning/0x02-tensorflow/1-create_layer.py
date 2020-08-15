#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def create_layer(prev, n, activation):
    """ create layer function """
    linear_model = tf.layers.dense(prev, units=n, activation=activation,
                                   name="layer")
    init = tf.contrib.layers.variance_scaling_initializer(prev, mode="FAN_AVG")
    """sess = tf.Session()
    sess.run(init) """
    return(linear_model)
