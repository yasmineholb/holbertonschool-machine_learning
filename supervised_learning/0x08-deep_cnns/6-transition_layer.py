#!/usr/bin/env python3
""" transition_layer """
import tensorflow.keras as K


def transition_layer(X, nb_filters, compression):
    """ Function that builds a transition layer as
        described in Densely Connected Convolutional Networks """
    he_init = K.initializers.he_normal()
    nb_f = int(nb_filters*compression)
    batchn1 = K.layers.BatchNormalization(axis=3)(X)
    act_1 = K.layers.Activation('relu')(batchn1)
    conv_1 = K.layers.Conv2D(filters=nb_f,
                             kernel_size=(1, 1),
                             padding="same",
                             kernel_initializer=he_init)(act_1)
    avg = K.layers.AveragePooling2D(pool_size=(2, 2),
                                    strides=(2, 2))(conv_1)
    return avg, nb_f
