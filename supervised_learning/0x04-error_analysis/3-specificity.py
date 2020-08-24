#!/usr/bin/env python3
""" Specificity matrix """
import numpy as np


def specificity(confusion):
    """ specificity """
    classes = np.shape(confusion)[0]
    res = np.ones(classes)
    for i in range(classes):
        A = np.ones(np.shape(confusion))
        A[:, i] = np.zeros(classes)
        A[i, :] = np.zeros(classes)
        S = sum(sum(A * confusion))
        res[i] = S / (S + sum(confusion[:, i]) - confusion[i, i])
    return res
