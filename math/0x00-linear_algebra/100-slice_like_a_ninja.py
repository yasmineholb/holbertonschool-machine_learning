#!/usr/bin/env python3
""" slice  function"""
import numpy as np


def np_slice(matrix, axes={}):
    new = []
    for key, value in axes.items():
        new.append(slice(None))
        new.append(slice(*value))
    return(matrix[tuple(new)])
