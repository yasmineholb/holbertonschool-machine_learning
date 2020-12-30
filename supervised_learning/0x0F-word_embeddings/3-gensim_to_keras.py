#!/usr/bin/env python3
""" Extract Word2Vec """

def gensim_to_keras(model):
    """ Function that that converts a gensim
        word2vec model to a keras Embedding layer """
    return model.wv.get_keras_embedding(train_embeddings=False)
