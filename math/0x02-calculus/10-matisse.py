#!/usr/bin/env python3
""" derivate function"""


def poly_derivative(poly):
    """ function derivate"""
    x = 0
    m = []
    p = [0]
    if type(poly) is not list:
        return None
    if len(poly) == 0:
        return None
    if len(poly) == 1:
        return(p)
    for i in range(len(poly)):
        if type(poly[i]) is not int:
            return(None)
    if poly is None:
        return None
    for i in range(1, len(poly)):
        x = poly[i] * i
        m.append(x)
    return m
