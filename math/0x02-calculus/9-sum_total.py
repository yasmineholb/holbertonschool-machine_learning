#!/usr/bin/env python3
""" sum """


def summation_i_squared(n):
    """sum function """
    if n is None or n < 1:
        return(None)
    return(int(((1/3)*(n**3))+((1/2)*(n**2))+(1/6)*n))
