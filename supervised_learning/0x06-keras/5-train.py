#!/usr/bin/env python3
""" train model """
import tensorflow.keras as K


def def train_model(network, data, labels, batch_size, epochs,
                    validation_data=None, verbose=True, shuffle=False):
    """ Function that trains a model using mini-batch
        gradient descent """
    history = network.fit(x=data, y=labels, epochs=epochs, verbose=verbose,
                          batch_size=batch_size,
                          validation_data=validation_data,
                          shuffle=shuffle)
    return history
