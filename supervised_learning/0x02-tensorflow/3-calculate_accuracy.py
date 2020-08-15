#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """ calculate function """
    acc = tf.metrics.accuracy(y, predictions=y_pred)
    return acc
