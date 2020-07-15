#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    """ cat matrices """
    if axis == 0:
        if len(mat1[0]) == len(mat2[0]):
            m = mat1 + mat2
            return(m)
        else:
            return(None)
    elif axis == 1:
        if len(mat1) == len(mat2):
            n = []
            for i in range(len(mat1)):
                m = mat1[i] + mat2[i]
                n.append(m)
            return(n)
        else:
            return(None)
    else:
        return(None)
