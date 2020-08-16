#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """ calculate function """
    """acc = tf.metrics.accuracy(y, predictions=y_pred)"""
    """cost =tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits = y_pred, labels = y))"""
    acc = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
        logits=y_pred, labels=y))
    return acc
