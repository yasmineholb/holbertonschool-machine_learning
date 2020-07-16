#!/usr/bin/env python3
""" slice  function"""


def np_slice(matrix, axes={}):
    new = []
    for val in range(len(matrix.shape)):
        t = slice(*axes.get(val, (None, None)))
        new.append(t)
    return(matrix[tuple(new)])
