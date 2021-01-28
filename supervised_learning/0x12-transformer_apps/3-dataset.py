#!/usr/bin/env python3
"""Class Dataset"""

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds


class Dataset():
    """ Dataset class"""

    def __init__(self):
        """ Function that initializes the dataset """

        def filter_max_length(x, y, max_length=max_len):
            """ max length function """
            return tf.logical_and(tf.size(x) <= max_length,
                                  tf.size(y) <= max_length)
        exp, metadata = tfds.load('ted_hrlr_translate/pt_to_en',
                                       with_info=True,
                                       as_supervised=True)
        self.data_train = exp['train']
        self.data_valid = exp['validation']
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)
        self.data_train = self.data_train.map(self.tf_encode)
        self.data_train = self.data_train.filter(filter_max_length)
        self.data_train = self.data_train.cache()
        shuff_met = metadata.splits['train'].num_examples
        self.data_train = self.data_train.shuffle(shuff_met)
        pad_shape = ([None], [None])
        self.data_train = self.data_train.padded_batch(batch_size,
                                                       padded_shapes=pad_shape)
        exp = tf.data.experimental.AUTOTUNE
        self.data_train = self.data_train.prefetch(zxp)
        self.data_valid = self.data_valid.map(self.tf_encode)
        self.data_valid = self.data_valid.filter(filter_max_length)
        self.data_valid = self.data_valid.padded_batch(batch_size,
                                                       padded_shapes=pad_shape)

    def tokenize_dataset(self, data):
        """ Function that hat creates sub-word tokenizers for our dataset """
        tokenizer_en = tfds.features.text.SubwordTextEncoder.build_from_corpus(
            (en.numpy() for pt, en in data), target_vocab_size=2 ** 15)
        tokenizer_pt = tfds.features.text.SubwordTextEncoder.build_from_corpus(
            (pt.numpy() for pt, en in data), target_vocab_size=2 ** 15)
        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        """ Function that encodes a translation into tokens """
        pt_tokens = [self.tokenizer_pt.vocab_size] + self.tokenizer_pt.encode(
            pt.numpy()) + [self.tokenizer_pt.vocab_size + 1]
        en_tokens = [self.tokenizer_en.vocab_size] + self.tokenizer_en.encode(
            en.numpy()) + [self.tokenizer_en.vocab_size + 1]
        return pt_tokens, en_tokens

    def tf_encode(self, pt, en):
        """ Function that acts as a tensorflow
            wrapper for the encode instance method """
        res_pt, res_en = tf.py_function(self.encode,
                                        [pt, en],
                                        [tf.int64, tf.int64])
        res_pt.set_shape([None])
        res_en.set_shape([None])
        return res_pt, res_en
