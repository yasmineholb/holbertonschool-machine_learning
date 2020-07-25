#!/usr/bin/env python3
""" sum """


def summation_i_squared(n):
    """sum function """
    if type(n) is not int and type(n) is not float:
        return None
    if n is None or n < 1:
        return(None)
    if n == 1:
        return 1
    return(int(((1/3)*(n**3))+((1/2)*(n**2))+(1/6)*n))
