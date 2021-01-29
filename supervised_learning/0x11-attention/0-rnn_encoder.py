#!/usr/bin/env python3
""" RNN encoder class """

import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """ Rnn encoder class """
    def __init__(self, vocab, embedding, units, batch):
        """ Function that initializes variables """
        super(RNNEncoder, self).__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(vocab, embedding)
        self.gru = tf.keras.layers.GRU(units,
                                       recurrent_initializer='glorot_uniform',
                                       return_sequences=True,
                                       return_state=True)

    def initialize_hidden_state(self):
        """ Function that initializes the hidden
            states for the RNN cell to a tensor of zeros """
        initializer = tf.keras.initializers.Zeros()
        hidden = initializer(shape=(self.batch, self.units))
        return hidden

    def call(self, x, initial):
        """ Function that returns outputs, hidden"""
        emb = self.embedding(x)
        outputs, hidden = self.gru(emb,
                                   initial_state=initial)
        return outputs, hidden
