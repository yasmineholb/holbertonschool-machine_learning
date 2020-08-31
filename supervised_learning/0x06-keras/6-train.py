#!/usr/bin/env python3
""" train model """
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """ Function that train the model using early stopping """
    if early_stopping is True:
        if validation_data is not None:
            es = K.callbacks.EarlyStopping(monitor='val_loss',
                                           mode='min', patience=patience)
            history = network.fit(x=data, y=labels, epochs=epochs,
                                  verbose=verbose,
                                  batch_size=batch_size,
                                  validation_data=validation_data,
                                  shuffle=shuffle, callbacks=[es])
        else:
            history = network.fit(x=data, y=labels, epochs=epochs,
                                  verbose=verbose,
                                  batch_size=batch_size,
                                  validation_data=validation_data,
                                  shuffle=shuffle)
    else:
        history = network.fit(x=data, y=labels, epochs=epochs, verbose=verbose,
                              batch_size=batch_size,
                              validation_data=validation_data,
                              shuffle=shuffle)
    return history
