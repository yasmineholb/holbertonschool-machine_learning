#!/usr/bin/env python3
""" Kmeans """
import sklearn.cluster


def kmeans(X, k):
    """ Function that performs K-means on a dataset """
    Km = sklearn.cluster.KMeans(n_clusters=k).fit(X)
    C = Km.cluster_centers_
    clss = Km.labels_
    return C, clss
