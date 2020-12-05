#!/usr/bin/env python3
""" vanilla Autoencoder """
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """ Function that creates an autoencoder """
    inp = keras.Input(shape=(input_dims,))
    hidden = keras.layers.Dense(units=hidden_layers[0], activation='relu')
    prev = hidden(inp)
    for i in range(1, len(hidden_layers)):
        prev = keras.layers.Dense(units=hidden_layers[i],
                                  activation='relu')(prev)
    lat = keras.layers.Dense(units=latent_dims, activation='relu')(prev)
    enc = keras.Model(inp, lat)
    inp = keras.Input(shape=(latent_dims,))
    hidd = keras.layers.Dense(units=hidden_layers[-1],
                              activation='relu')
    prev = hidd(inp)
    for k in range(len(hidden_layers) - 2, -1, -1):
        hidd = keras.layers.Dense(units=hidden_layers[k],
                                  activation='relu')
        prev = hidd(prev)
    layer = keras.layers.Dense(units=input_dims, activation='sigmoid')(prev)
    dec = keras.Model(inp, layer)
    inputt = keras.Input(shape=(input_dims,))
    encoder = enc(inputt)
    decoder = dec(encoder)
    auto = keras.Model(inputt, decoder)
    auto.compile(loss='binary_crossentropy', optimizer='adam')
    return enc, dec, auto
