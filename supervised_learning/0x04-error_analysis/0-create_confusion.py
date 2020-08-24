#!/usr/bin/env python3
""" confusion matrix """
import numpy as np


def create_confusion_matrix(labels, logits):
    """ create confusion """
    m, classes = np.shape(labels)
    res = np.zeros((classes, classes))
    for k in range(m):
        i = np.where(labels[k, :] == 1)
        j = np.where(logits[k, :] == 1)
        res[i, j] += 1
    return res
