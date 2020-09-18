#!/usr/bin/env python3
""" densenet121 """
import tensorflow.keras as K
dense_block = __import__('5-dense_block').dense_block
transition_layer = __import__('6-transition_layer').transition_layer


def densenet121(growth_rate=32, compression=1.0):
    """ Function that builds the DenseNet-121 architecture
        as described in Densely Connected Convolutional Networks """
    he_init = K.initializers.he_normal()
    inp = K.Input(shape=(224, 224, 3))
    batch_1 = K.layers.BatchNormalization(axis=3)(inp)
    act1 = K.layers.Activation('relu')(batch_1)
    conv_f1 = K.layers.Conv2D(filters=2*growth_rate, kernel_size=(7, 7),
                              padding='same',
                              strides=(2, 2),
                              kernel_initializer=he_init)(act1)
    pool_1 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                   strides=(2, 2),
                                   padding="same")(conv_f1)
    dense1, nb_f1 = dense_block(pool_1, 2*growth_rate, growth_rate, 6)
    trans1, nb_f2 = transition_layer(dense1, nb_f1, compression)
    dense2, nb_f3 = dense_block(trans1, nb_f2, growth_rate, 12)
    trans2, nb_f4 = transition_layer(dense2, nb_f3, compression)
    dense3, nb_f5 = dense_block(trans2, nb_f4, growth_rate, 24)
    trans3, nb_f6 = transition_layer(dense3, nb_f5, compression)
    dense4, nb_f7 = dense_block(trans3, nb_f6, growth_rate, 16)
    avg = K.layers.AveragePooling2D(pool_size=(7, 7),
                                    strides=(1, 1))(dense4)
    res = K.layers.Dense(units=1000, activation='softmax',
                         kernel_initializer=he_init)(avg)
    model = K.models.Model(inputs=inp, outputs=res)
    return model
