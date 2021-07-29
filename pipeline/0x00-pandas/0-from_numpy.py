#!/usr/bin/env python3
""" From Numpy """
import pandas as pd


def from_numpy(array):
    """ Function that that creates a pd.DataFrame from a np.ndarray """
    return pd.DataFrame(array)
