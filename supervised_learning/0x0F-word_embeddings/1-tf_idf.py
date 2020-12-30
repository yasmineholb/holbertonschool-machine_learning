#!/usr/bin/env python3
""" TF-IDF  """

from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(sentences, vocab=None):
    """ Function that creates a TF-IDF
        embedding """
    vect = TfidfVectorizer(vocabulary=vocab)
    ft = vect.fit_transform(sentences)
    features = vect.get_feature_names()
    embeddings = ft.toarray()
    return embeddings, features
