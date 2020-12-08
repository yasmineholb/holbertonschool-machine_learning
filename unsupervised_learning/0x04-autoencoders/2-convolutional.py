#!/usr/bin/env python3
""" Convolutional Autoencoder """
import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    """ Function that creates a convolutional autoencoder """
    inp = keras.Input(shape=input_dims)
    conv = keras.layers.Conv2D(filters=filters[0], kernel_size=3,
                               padding='same', activation='relu')(inp)
    encoded = keras.layers.MaxPooling2D(pool_size=(2, 2),
                                        padding="same")(conv)
    for i in range(1, len(filters)):
        conv = keras.layers.Conv2D(filters=filters[i],
                                   kernel_size=3, padding='same',
                                   activation='relu')(encoded)
        encoded = keras.layers.MaxPooling2D(pool_size=(2, 2),
                                            padding="same")(conv)
    lat = encoded
    enc = keras.Model(inp, lat)
    decode = keras.Input(shape=latent_dims)
    dec_conv = keras.layers.Conv2D(filters=filters[-1], kernel_size=3,
                                   padding='same', activation='relu')(decode)
    decoded = keras.layers.UpSampling2D((2, 2))(dec_conv)
    for k in range(len(filters) - 2, 0, -1):
        dec_conv = keras.layers.Conv2D(filters=filters[k],
                                       kernel_size=3,
                                       padding='same',
                                       activation='relu')(decoded)
        decoded = keras.layers.UpSampling2D((2, 2))(dec_conv)
    dec_conv = keras.layers.Conv2D(filters=filters[0], kernel_size=3,
                                   padding='valid', activation='relu')(decoded)

    decoded = keras.layers.UpSampling2D((2, 2))(dec_conv)
    out = keras.layers.Conv2D(filters=input_dims[-1], kernel_size=3,
                              padding='same', activation='sigmoid')(decoded)
    dec = keras.Model(decode, out)
    inputt = keras.Input(shape=(input_dims))
    encoder = enc(inputt)
    decoder = dec(encoder)
    auto = keras.Model(inputt, decoder)
    auto.compile(loss='binary_crossentropy', optimizer='adam')
    return enc, dec, auto
