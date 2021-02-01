#!/usr/bin/env python3
""" RNN Decoder """

import tensorflow as tf
SelfAttention = __import__('1-self_attention').SelfAttention


class RNNDecoder(tf.keras.layers.Layer):
    """
    """
    def __init__(self, vocab, embedding, units, batch):
        """ Initialisation function """
        super(RNNDecoder, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab, embedding)
        self.gru = tf.keras.layers.GRU(units,
                                       recurrent_initializer='glorot_uniform',
                                       return_sequences=True,
                                       return_state=True)
        self.F = tf.keras.layers.Dense(vocab)
        self.attention = SelfAttention(units)

    def call(self, x, s_prev, hidden_states):
        """ Function that returns two tensors """
        cn, att = self.attention(s_prev, hidden_states)
        x = self.embedding(x)
        x = tf.concat([tf.expand_dims(cn, 1), x], axis=-1)
        output, s = self.gru(x)
        output = tf.reshape(output, (-1, output.shape[2]))
        y = self.F(output)
        return y, s
