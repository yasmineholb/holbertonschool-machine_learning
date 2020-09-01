#!/usr/bin/env python3
""" train model """
import tensorflow.keras as K


def save_weights(network, filename,
                 save_format='h5'):
    """ Function that saves an entire
        model """
    network.save_weights(filename,
                         save_format=save_format)
    return None


def load_weights(network, filename):
    """ Function that loads a model’s
        weights: """
    network.load_weights(filename)
    return None
