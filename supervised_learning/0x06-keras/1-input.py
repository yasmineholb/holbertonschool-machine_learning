#!/usr/bin/env python3
""" build model with input """
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """ Function that builds a neural network with the Keras
        library """
    inpt = K.Input((nx,))
    for i in range(len(layers)):
        k_r = K.regularizers.l2(lambtha)
        if i == 0:
            x = K.layers.Dense(layers[i], activation=activations[i],
                               input_dim=nx, kernel_regularizer=k_r)(inpt)
        else:
            x = K.layers.Dense(layers[i], activation=activations[i],
                               input_dim=nx, kernel_regularizer=k_r)(x)
        if i < len(layers) - 1:
            x = K.layers.Dropout(1-keep_prob)(x)
    m = K.Model(inpt, x)
    return m
