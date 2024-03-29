#!/usr/bin/env python3
""" Crop """
import tensorflow as tf


def crop_image(image, size):
    """ Function that performs a random crop of an image """
    return tf.image.random_crop(image, size)
