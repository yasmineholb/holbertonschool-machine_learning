#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def calculate_loss(y, y_pred):
    """ calculates the loss """
    loss = tf.nn.softmax_cross_entropy_with_logits(y, y_pred)
    return(loss)
