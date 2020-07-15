#!/usr/bin/env python3
""" add matrices"""


def add_matrices2D(mat1, mat2):
    """add function """
    s = len(mat1)
    s2 = len(mat1[0])
    if abs(s - len(mat2)) != 0 or abs(s2 - len(mat2[0])) != 0:
        return(None)
    tab = []
    j = 0
    for i in range(s):
        tab2 = []
        for j in range(s2):
            tab2.append(mat1[i][j] + mat2[i][j])
        tab.append(tab2)
    return(tab)
