#!/usr/bin/env python3
""" dense_block """
import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """ Function that builds a dense block as described
        in Densely Connected Convolutional Networks """
    he_init = K.initializers.he_normal()
    for i in range(layers):
        batchn1 = K.layers.BatchNormalization(axis=3)(X)
        act_1 = K.layers.Activation('relu')(batchn1)
        conv_1 = K.layers.Conv2D(filters=(4 * growth_rate),
                                 kernel_size=(1, 1),
                                 padding="same",
                                 kernel_initializer=he_init)(act_1)
        batchn2 = K.layers.BatchNormalization(axis=3)(conv_1)
        act_2 = K.layers.Activation('relu')(batchn2)
        conv_2 = K.layers.Conv2D(filters=growth_rate,
                                 kernel_size=(3, 3),
                                 padding="same",
                                 kernel_initializer=he_init)(act_2)
        X = K.layers.concatenate([X, conv_2])
        nb_filters += growth_rate
    return X, nb_filters
