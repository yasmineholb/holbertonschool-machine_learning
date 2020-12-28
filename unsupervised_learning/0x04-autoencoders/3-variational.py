#!/usr/bin/env python3
""" Variational Autoencoder """

import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """ Function that creates a variational autoencoder """
    inputt = keras.Input(shape=(input_dims,))
    hidden = keras.layers.Dense(units=hidden_layers[0], activation='relu')
    prev = hidden(inputt)
    for i in range(1, len(hidden_layers)):
        hidden_ly = keras.layers.Dense(units=hidden_layers[i],
                                       activation='relu')
        prev = hidden(prev)
    latent = keras.layers.Dense(units=latent_dims, activation=None)
    mean = latent(prev)
    sigma = latent(prev)

    def sampling(args):
        mean, sigma = args
        eps = keras.backend.random_normal(shape=(latent_dims,), mean=0.0,
                                          stddev=1.0)
        return mean + keras.backend.exp(sigma) * eps

    lam = keras.layers.Lambda(sampling, output_shape=(
        latent_dims,))([mean, sigma])
    enc = keras.models.Model(inputt, lam)
    input_l = keras.Input(shape=(latent_dims,))
    for i in range(len(hidden_layers) - 1, -1, -1):
        if i == len(hidden_layers) - 1:
            decc = keras.layers.Dense(
                hidden_layers[i], activation='relu')(input_l)
        else:
            decc = keras.layers.Dense(
                hidden_layers[i], activation='relu')(decc)
    decc = keras.layers.Dense(input_dims, activation='sigmoid')(decc)
    dec = keras.models.Model(input_l, decc)
    dec.summary()
    x = keras.Input(shape=(input_dims,))
    z_enc = enc(x)
    x_decoder_mean = dec(z_enc)
    autoenc = keras.models.Model(inputs=x, outputs=x_decoder_mean)
    autoenc.summary()

    def vae_loss(x, x_decoder_mean):
        loss_bn = keras.backend.binary_crossentropy(x, x_decoder_mean)
        loss_back = - 0.5 * keras.backend.mean(1 + sigma -
                                               keras.backend.square(mean) -
                                               keras.backend.exp(sigma),
                                               axis=-1)
        return loss_bn + loss_back
    autoenc.compile(optimizer='Adam', loss=vae_loss)
    return enc, dec, autoenc
