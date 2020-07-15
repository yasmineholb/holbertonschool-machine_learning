#!/usr/bin/env python3
""" mat_mul"""


def mat_mul(mat1, mat2):
    """ mat function """
    li1, li2 = len(mat1), len(mat2)
    col1, col2 = len(mat1[0]), len(mat2[0])
    if col1 == li2:
        ta = []
        for i in range(li1):
            ta2 = []
            for j in range(col2):
                somme = 0
                for k in range(col1):
                    somme += mat1[i][k] * mat2[k][j]
                ta2.append(somme)
            ta.append(ta2)
        return ta
    else:
        return(None)
