#!/usr/bin/env python3
""" derivate function"""


def poly_derivative(poly):
    """ function derivate"""
    x = 0
    m = []
    p = [0]
    if len(poly) == 1:
        return(p)
    if poly is None:
        return None
    for i in range(1, len(poly)):
        x = poly[i] * i
        m.append(x)
    return m
