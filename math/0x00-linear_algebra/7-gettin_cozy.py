#!/usr/bin/env python3
""" cat fn """
import copy


def cat_matrices2D(mat1, mat2, axis=0):
    """ cat matrices """
    matt1 = copy.deepcopy(mat1)
    matt2 = copy.deepcopy(mat2)
    if axis == 0:
        if len(mat1[0]) == len(mat2[0]):
            m = matt1 + matt2
            return(m)
        else:
            return(None)
    elif axis == 1:
        if len(mat1) == len(mat2):
            n = []
            for i in range(len(matt1)):
                m = matt1[i] + matt2[i]
                n.append(m)
            return(n)
        else:
            return(None)
