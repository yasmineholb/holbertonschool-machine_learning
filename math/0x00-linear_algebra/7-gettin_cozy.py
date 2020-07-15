#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    if axis == 0:
        m = mat1 + mat2
        return(m)
    elif axis == 1:
        n = []
        for i in range(len(mat1)):
            m = mat1[i] + mat2[i]
            n.append(m)
        return(n)
