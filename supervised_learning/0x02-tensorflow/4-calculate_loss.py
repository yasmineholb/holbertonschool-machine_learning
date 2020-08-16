#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def calculate_loss(y, y_pred):
    """ calculates the loss """
    loss = tf.losses.softmax_cross_entropy(y, y_pred)
    return(loss)
