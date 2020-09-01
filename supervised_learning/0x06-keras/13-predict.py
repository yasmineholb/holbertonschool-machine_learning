#!/usr/bin/env python3
""" test model """
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """ Function that makes a prediction using a neural network """
    pr = network.predict(data, verbose=verbose)
    return pr
