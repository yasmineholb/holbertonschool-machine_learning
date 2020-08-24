#!/usr/bin/env python3
""" precision matrix """
import numpy as np


def precision(confusion):
    """ precision """
    diag = np.diagonal(confusion)
    conf = np.sum(confusion, axis=0)
    res = diag / conf
    return res
