#!/usr/bin/env python3
""" train model """
import tensorflow.keras as K


def save_model(network, filename):
    """ Function that saves an entire
        model """
    network.save(filename)
    return None


def load_model(filename):
    """ Function that loads an
        entire model """
    ld = K.models.load_model(filename)
    return ld
