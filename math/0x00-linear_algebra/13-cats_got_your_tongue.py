#!/usr/bin/env python3
import numpy as np
""" cat function """


def np_cat(mat1, mat2, axis=0):
    """ cat function """
    return(np.concatenate((mat1, mat2), axis))
