#!/usr/bin/env python3
""" Adam optimizer """
import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """ Function that sets up Adam optimization for
        a keras model with categorical crossentropy
        loss and accuracy metrics """
    opt = K.optimizers.Adam(alpha, beta1, beta2)
    lo = 'categorical_crossentropy'
    network.compile(opt, metrics=['accuracy'], loss=lo)
    return None
