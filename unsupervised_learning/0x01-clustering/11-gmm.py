#!/usr/bin/env python3
""" gmm """
import sklearn.mixture


def gmm(X, k):
    """ Function that calculates a
        GMM from a dataset """
    gauss = sklearn.mixture.GaussianMixture(n_components=k)
    gauss = gauss.fit(X)
    pi = gauss.weights_
    m = gauss.means_
    S = gauss.covariances_
    clss = gauss.predict(X)
    bic = gauss.bic(X)
    return pi, m, S, clss, bic
