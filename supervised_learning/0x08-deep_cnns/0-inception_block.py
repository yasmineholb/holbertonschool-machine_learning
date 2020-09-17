#!/usr/bin/env python3
""" inception_block """
import tensorflow.keras as K


def inception_block(A_prev, filters):
    """ Function that builds an inception
        block as described in Going Deeper with
        Convolutions (2014) """
    F1, F3R, F3, F5R, F5, FPP = filters
    he_init = K.initializers.he_normal()
    conv_f1 = K.layers.Conv2D(filters=F1, kernel_size=(1, 1), padding='same',
                              activation='relu',
                              kernel_initializer=he_init)(A_prev)
    conv_f3R = K.layers.Conv2D(filters=F3R, kernel_size=(1, 1), padding='same',
                               activation='relu',
                               kernel_initializer=he_init)(A_prev)
    conv_f3 = K.layers.Conv2D(filters=F3, kernel_size=(3, 3), padding='same',
                              activation='relu',
                              kernel_initializer=he_init)(conv_f3R)
    conv_f5R = K.layers.Conv2D(filters=F5R, kernel_size=(1, 1), padding='same',
                               activation='relu',
                               kernel_initializer=he_init)(A_prev)
    conv_f5 = K.layers.Conv2D(filters=F5, kernel_size=(5, 5), padding='same',
                              activation='relu',
                              kernel_initializer=he_init)(conv_f5R)
    m_pool = K.layers.MaxPooling2D(pool_size=(3, 3), strides=(1, 1),
                                   padding='same')(A_prev)
    conv_fPP = K.layers.Conv2D(filters=FPP, kernel_size=(1, 1), padding='same',
                               activation='relu',
                               kernel_initializer=he_init)(m_pool)
    incep = K.layers.concatenate([conv_f1, conv_f3, conv_f5, conv_fPP])
    return incep
