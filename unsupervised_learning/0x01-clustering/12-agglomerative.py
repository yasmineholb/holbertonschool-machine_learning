#!/usr/bin/env python3
""" agglomerative """
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """ Function that performs agglomerative
        clustering on a dataset """
    hr = scipy.cluster.hierarchy.linkage(X, method='ward')
    clss = scipy.cluster.hierarchy.fcluster(Z=hr, t=dist,
                                            criterion="distance")
    plt.figure()
    scipy.cluster.hierarchy.dendrogram(Z=hr, color_threshold=dist)
    plt.show()
    return clss
