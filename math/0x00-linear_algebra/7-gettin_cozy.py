#!/usr/bin/env python3
import copy
""" cat fn """


def cat_matrices2D(mat1, mat2, axis=0):
    """ cat matrices """
    matt1 = copy.deepcopy(mat1)
    matt2 = copy.deepcopy(mat2)
    if axis == 0:
        m = matt1 + matt2
        return(m)
    elif axis == 1:
        n = []
        for i in range(len(matt1)):
            m = matt1[i] + matt2[i]
            n.append(m)
        return(n)
