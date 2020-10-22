#!/usr/bin/env python3
""" cofactor """


def determinant(matrix):
    """ Function that calculates the determinant of a matrix """
    len1 = len(matrix)
    if matrix == [[]]:
        return 1
    if type(matrix[0]) is not list or type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    elif len(matrix[0]) != len1:
        raise ValueError("matrix must be a square matrix")
    for i in range(1, len1):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix[i]) != len1:
            raise ValueError("matrix must be a square matrix")
    if len1 == 1 and len(matrix[0]) == 0:
        return 1
    if len1 == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    if len1 == 2:
        return (matrix[0][0]) * matrix[1][1] - (matrix[0][1] * matrix[1][0])
    else:
        S = 0
        for i in range(len1):
            a = list(range(len1))
            a.pop(i)
            S += matrix[0][i] * ((-1) ** (i)) * determinant(
                [[matrix[i][j] for j in a]
                 for i in list(range(1, len1))])
        return S


def cofactor(matrix):
    """ Function that calculates the
        cofactor matrix of a matrix """
    len1 = len(matrix)
    if matrix == []:
        raise TypeError("matrix must be a list of lists")
    if type(matrix[0]) is not list or type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    elif len(matrix[0]) != len1:
        raise ValueError("matrix must be a non-empty square matrix")
    for i in range(1, len1):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix[i]) != len1:
            raise ValueError("matrix must be a non-empty square matrix")
    if len1 == 1:
        return [[1]]
    else:
        mat = []
        for i in range(len1):
            t = []
            s = 0
            while (s < len1):
                new = []
                new += [list(j) for j in matrix]
                new.pop(i)
                mat1 = []
                for k in new:
                    k.pop(s)
                mat1 += [k for k in new]
                t.append(determinant(mat1))
                s += 1
            mat.append(t)
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] *= (-1) ** (i+j)
    return mat
