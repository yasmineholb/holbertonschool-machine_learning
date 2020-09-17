#!/usr/bin/env python3
""" inception_network """
import tensorflow.keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """ Function that builds the inception network as
        described in Going Deeper with Convolutions (2014) """
    Inp = K.Input(shape=(224, 224, 3))
    he_init = K.initializers.he_normal()
    conv1 = K.layers.Conv2D(filters=64, kernel_size=(7, 7),
                            strides=(2, 2), padding='same',
                            activation='relu',
                            kernel_initializer=he_init)(Inp)
    maxp1 = K.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2),
                                  padding='same')(conv1)
    conv2 = K.layers.Conv2D(filters=64, kernel_size=(1, 1),
                            activation='relu',
                            kernel_initializer=he_init)(maxp1)
    conv3 = K.layers.Conv2D(filters=192, kernel_size=(3, 3),
                            padding='same', activation='relu',
                            kernel_initializer=he_init)(conv2)
    maxp2 = K.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2),
                                  padding='same')(conv3)
    incep_1 = inception_block(maxp2, [64, 96, 128, 16, 32, 32])
    incep_2 = inception_block(incep_1, [128, 128, 192, 32, 96, 64])
    maxp3 = K.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2),
                                  padding='same')(incep_2)
    incep_3 = inception_block(maxp3, [192, 96, 208, 16, 48, 64])
    incep_4 = inception_block(incep_3, [160, 112, 224, 24, 64, 64])
    incep_5 = inception_block(incep_4, [128, 128, 256, 24, 64, 64])
    incep_6 = inception_block(incep_5, [112, 144, 288, 32, 64, 64])
    incep_7 = inception_block(incep_6, [256, 160, 320, 32, 128, 128])
    maxp_lay4 = K.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2),
                                      padding='same')
    maxpool4 = maxp_lay4(incep_7)
    incep_8 = inception_block(maxpool4, [256, 160, 320, 32, 128, 128])
    incep_9 = inception_block(incep_8, [384, 192, 384, 48, 128, 128])
    avgp1 = K.layers.AveragePooling2D(pool_size=(7, 7),
                                      strides=(1, 1))(incep_9)
    drop = K.layers.Dropout(0.4)(avgp1)
    res = K.layers.Dense(units=1000, activation='softmax',
                         kernel_initializer=he_init)(drop)
    model = K.models.Model(inputs=Inp, outputs=res)
    return model
