#!/usr/bin/env python3
""" From File """
import pandas as pd


def from_file(filename, delimiter):
    """ Function that  that loads data from a file as a pd.DataFrame """
    return pd.read_csv(filename, delimiter=delimiter)
