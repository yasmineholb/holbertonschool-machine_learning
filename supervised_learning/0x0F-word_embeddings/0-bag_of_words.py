#!/usr/bin/env python3
""" Bag of words """

from sklearn.feature_extraction.text import CountVectorizer


def bag_of_words(sentences, vocab=None):
    """ Function that creates a bag of
        words embedding matrix """
    vect = CountVectorizer(vocabulary=vocab)
    ft = vect.fit_transform(sentences)
    features = vect.get_feature_names()
    embeddings = ft.toarray()
    return embeddings, features
