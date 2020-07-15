#!/usr/bin/env python3
""" wise elem """


def np_elementwise(mat1, mat2):
    """ np elem """
    return(mat1.__add__(mat2), mat1.__sub__(mat2),
           mat1.__mul__(mat2), mat1.__truediv__(mat2))
