#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """ calculate function """
    """acc = tf.accuracy(y, predictions=y_pred)
    cost =tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    logits = y_pred, labels = y))
    acc = tf.reduce_mean(tf.cast(ac, tf.float32))
    return acc
    ac = tf.equal(y, y_pred)
    accuracy = tf.reduce_mean(tf.cast(ac, tf.float32))
    return accuracy"""
    ac = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
    accuracy = tf.reduce_mean(tf.cast(ac, tf.float32))
    return accuracy
