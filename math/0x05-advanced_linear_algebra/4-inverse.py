#!/usr/bin/env python3
""" inverse """


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
    """ Function that calculates the cofactor matrix of a matrix """
    len1 = len(matrix)
    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    if type(matrix[0]) is not list or type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    elif len(matrix[0]) != len1:
        raise ValueError("matrix must be a non-empty square matrix")
    for i in range(1, len1):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix[i]) != len1:
            raise ValueError("matrix must be a non-empty square matrix")
    if len1 == 1 and len(matrix[0]) == 1:
        return [[1]]
    else:
        S = [[0 for i in range(len1)]for j in range(len1)]
        for i in range(len1):
            for j in range(len1):
                a = list(range(len1))
                b = list(range(len1))
                a.pop(i)
                b.pop(j)
                S[i][j] = ((-1) ** (i+j)) * determinant(
                    [[matrix[i][j] for j in b]
                     for i in a])
        return S


def matrix_transpose(matrix):
    """ transpose"""
    len1, len2 = len(matrix), len(matrix[0])
    s = []
    for i in range(len2):
        m = []
        for j in range(len1):
            m.append(matrix[j][i])
        s.append(m)
    return(s)


def adjugate(matrix):
    """ Function that calculates the adjugate matrix of a matrix """
    len1 = len(matrix)
    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    if type(matrix[0]) is not list or type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    elif len(matrix[0]) != len1:
        raise ValueError("matrix must be a non-empty square matrix")
    for i in range(1, len1):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix[i]) != len1:
            raise ValueError("matrix must be a non-empty square matrix")
    if len1 == 1 and len(matrix[0]) == 1:
        return [[1]]
    else:
        return matrix_transpose(cofactor(matrix))


def inverse(matrix):
    """ Function that calculates the inverse of a matrix """
    len1 = len(matrix)
    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    if type(matrix[0]) is not list or type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    elif len(matrix[0]) != len1:
        raise ValueError("matrix must be a non-empty square matrix")
    for i in range(1, len1):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a list of lists")
        if len(matrix[i]) != len1:
            raise ValueError("matrix must be a non-empty square matrix")
    if determinant(matrix) == 0:
        return None
    if len1 == 1 and len(matrix[0]) == 1:
        return [[1/matrix[0][0]]]
    else:
        d = determinant(matrix)
        A = adjugate(matrix)
        return [[A[i][j] / d for j in range(len1)]for i in range(len1)]
