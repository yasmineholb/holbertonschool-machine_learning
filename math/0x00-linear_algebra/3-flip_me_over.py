#!/usr/bin/env python3
def matrix_transpose(matrix):
    len1, len2 = len(matrix), len(matrix[0])
    s = []
    for i in range(len2):
        m = []
        for j in range(len1):
            m.append(matrix[j][i])
        s.append(m)
    return(s)
