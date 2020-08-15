#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def create_placeholders(nx, classes):
    """ placeholders """
    x = tf.placeholder(tf.float32, [None, nx], name="x")
    y = tf.placeholder(tf.float32, [None, classes], name="y")
    """with tf.Session() as sess:
        return(sess.run(y, feed_dict={x: 0}))"""
    return x, y
