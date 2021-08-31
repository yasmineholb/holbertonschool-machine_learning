#!/usr/bin/env python3
""" Shear """
import tensorflow as tf


def shear_image(image, intensity):
    """ Function that  randomly shears an image """
    image = tf.expand_dims(image, axis=0)
    dtg = (tf.keras.preprocessing.image.ImageDataGenerator
           (shear_range=intensity))
    dtg.fit(x=image)
    new_image = dtg.flow(image)
    new_image = new_image.next()[0].astype("int")
    return new_image
