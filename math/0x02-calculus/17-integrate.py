#!/usr/bin/env python3
"""function integral """


def poly_integral(poly, C=0):
    """ function """
    if type(C) != int and type(C) != float:
        return None
    elif poly == []:
        return None
    elif type(poly) == list:
        lis = [C]
        for i in range(len(poly)):
            if int(poly[i]/(i+1)) == poly[i]/(i+1):
                lis.append(int(poly[i]/(i+1)))
            else:
                lis.append(poly[i]/(i+1))
        return lis
    else:
        return None
