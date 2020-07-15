#!/usr/bin/env python3
""" function"""
import numpy as np

def add_matrices(mat1, mat2):
    """add function """
    m1=np.asarray(mat1)
    m2=np.asarray(mat2)
    s=np.shape(m1)
    ss=np.shape(m2)
    if s == ss:
        if len(s) == 1:
            return np.ndarray.tolist(m1+m2)
        else:
            S=np.zeros(s)
            for i in range(s[0]):
                S[i,:]=m1[i,:]+m2[i,:]
        return(np.ndarray.tolist(S))
    else:
        return(None)
