#!/usr/bin/env python3
""" Create mask function """

import tensorflow.compat.v2 as tf


def create_masks(inputs, target):
    """ Function that creates all masks for training/validation """
    encoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    encoder_mask = encoder_mask[:, tf.newaxis, tf.newaxis, :]
    decoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    decoder_mask = decoder_mask[:, tf.newaxis, tf.newaxis, :]
    size = target.shape[1]
    look_ahead_mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
    dec_mask = tf.cast(tf.math.equal(target, 0), tf.float32)
    dec_mask = dec_mask[:, tf.newaxis, tf.newaxis, :]
    look_comb_mask = tf.maximum(dec_mask, look_ahead_mask)
    return encoder_mask, look_comb_mask, decoder_mask
