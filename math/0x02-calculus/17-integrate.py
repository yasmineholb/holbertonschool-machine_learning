#!/usr/bin/env python3
"""function integral """


def poly_integral(poly, C=0):
    """ function """
    if (type(C) is not int and type(C) is not float) or type(poly) is not list:
        return None
    elif poly is None or C is None:
        return None
    lis = [C]
    for i in range(len(poly)):
        if type(poly[i]) is not int:
            return(None)
        for i in range(len(poly)):
            if int(poly[i]/(i+1)) == poly[i]/(i+1):
                lis.append(int(poly[i]/(i+1)))
            else:
                lis.append(poly[i]/(i+1))
        return lis
    else:
        return None
