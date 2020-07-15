#!/usr/bin/env python3
def np_elementwise(mat1, mat2):
    return(mat1.__add__(mat2), mat1.__sub__(mat2),
           mat1.__mul__(mat2), mat1.__truediv__(mat2))
