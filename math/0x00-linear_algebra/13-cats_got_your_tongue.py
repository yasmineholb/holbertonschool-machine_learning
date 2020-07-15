#!/usr/bin/env python3
""" cat function """
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ cat function """
    return(np.concatenate((mat1, mat2), axis))
