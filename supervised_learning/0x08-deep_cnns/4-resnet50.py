#!/usr/bin/env python3
""" resnet50 """
import tensorflow.keras as K
identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    """ Function that builds the ResNet-50 architecture
        as described in Deep Residual Learning for Image
        Recognition (2015) """
    inp = K.Input(shape=(224, 224, 3))
    he_init = K.initializers.he_normal()
    conv_1 = K.layers.Conv2D(filters=64, kernel_size=(7, 7),
                             padding='same',
                             strides=(2, 2),
                             kernel_initializer=he_init)(inp)
    batch_1 = K.layers.BatchNormalization(axis=3)(conv_1)
    act1 = K.layers.Activation('relu')(batch_1)
    pool_1 = K.layers.MaxPooling2D(pool_size=(3, 3),
                                   strides=(2, 2),
                                   padding="same")(act1)
    proj_0 = projection_block(pool_1, [64, 64, 256], 1)
    id_1 = identity_block(proj_0, [64, 64, 256])
    id_2 = identity_block(id_1, [64, 64, 256])
    proj_1 = projection_block(id_2, [128, 128, 512])
    id_3 = identity_block(proj_1, [128, 128, 512])
    id_4 = identity_block(id_3, [128, 128, 512])
    id_5 = identity_block(id_4, [128, 128, 512])
    proj_2 = projection_block(id_5, [256, 256, 1024])
    id_6 = identity_block(proj_2, [256, 256, 1024])
    id_7 = identity_block(id_6, [256, 256, 1024])
    id_8 = identity_block(id_7, [256, 256, 1024])
    id_9 = identity_block(id_8, [256, 256, 1024])
    id_10 = identity_block(id_9, [256, 256, 1024])
    proj_3 = projection_block(id_10, [512, 512, 2048])
    id_11 = identity_block(proj_3, [512, 512, 2048])
    id_12 = identity_block(id_11, [512, 512, 2048])
    avg = K.layers.AveragePooling2D(pool_size=(7, 7),
                                    strides=(1, 1))(id_12)
    res = K.layers.Dense(units=1000, activation='softmax',
                         kernel_initializer=he_init)(avg)
    model = K.models.Model(inputs=inp, outputs=res)
    return model
