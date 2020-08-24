#!/usr/bin/env python3
""" confusion matrix """
import numpy as np


def sensitivity(confusion):
    """ sensitivity """
    diag = np.diagonal(confusion)
    conf = np.sum(confusion, axis=1)
    res = diag / conf
    return res
