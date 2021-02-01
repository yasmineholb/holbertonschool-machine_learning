#!/usr/bin/env python3
""" Scaled Dot Product Attention """

import tensorflow as tf


def sdp_attention(Q, K, V, mask=None):
    """ Function that calculates the scaled
        dot product attention """
    q = tf.matmul(Q, K, transpose_b=True)
    dk = tf.cast(tf.shape(K)[-1], tf.float32)
    sqr = q / tf.math.sqrt(dk)
    if mask is not None:
        sqr += (mask * -1e9)
    weights = tf.nn.softmax(sqr, axis=-1)
    output = tf.matmul(weights, V)
    return output, weights
