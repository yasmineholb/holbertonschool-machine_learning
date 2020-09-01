#!/usr/bin/env python3
""" build model with sequential """
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """ Function that builds a neural network with the Keras
        library """
    model = K.Sequential()
    for i in range(len(layers)):
        k_r = K.regularizers.l2(lambtha)
        model.add(K.layers.Dense(layers[i], activation=activations[i],
                                 input_dim=nx, kernel_regularizer=k_r))
        if i < len(layers) - 1:
            model.add(K.layers.Dropout(1-keep_prob))
        return model
