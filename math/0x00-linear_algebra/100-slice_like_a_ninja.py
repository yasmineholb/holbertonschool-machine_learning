#!/usr/bin/env python3
""" slice  function"""
import numpy as np


def np_slice(matrix, axes={}):
    new = []
    for val in range(len(matrix)):
        t = slice(*axes.get(val, (None, None)))
        new.append(t)
    return(matrix[tuple(new)])
