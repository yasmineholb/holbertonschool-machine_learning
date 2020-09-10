#!/usr/bin/env python3
""" LeNet-5 (Keras) """
import tensorflow.keras as K


def lenet5(X):
    """ Function that builds a modified version
        of the LeNet-5 architecture using keras """
    init = K.initializers.he_normal(seed=None)
    conv1 = K.layers.Conv2D(filters=6, kernel_size=(5, 5),
                            padding='same', activation='relu',
                            kernel_initializer=init)(X)
    pool1 = K.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(conv1)
    conv2 = K.layers.Conv2D(filters=16, kernel_size=(5, 5),
                            padding='valid', activation='relu',
                            kernel_initializer=init)(pool1)
    pool2 = K.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(conv2)
    flt = K.layers.Flatten()(pool2)
    n1 = K.layers.Dense(units=120, activation='relu',
                        kernel_initializer=init)(flt)
    n2 = K.layers.Dense(units=84, activation='relu',
                        kernel_initializer=init)(n1)
    n3 = K.layers.Dense(units=10, activation='softmax',
                        kernel_initializer=init)(n2)
    model = K.models.Model(inputs=X, outputs=n3)
    opt = K.optimizers.Adam()
    model.compile(loss='categorical_crossentropy', optimizer=opt,
                  metrics=['accuracy'])
    return model
