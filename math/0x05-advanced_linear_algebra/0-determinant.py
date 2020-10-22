def determinant(matrix):
    """ Function that calculates the determinant of a matrix """
    len1, len2 = len(matrix), len(matrix[0])
    if type(matrix[0]) is not list or type(matrix) is not list:
        raise TypeError("matrix must be a list of lists")
    elif matrix == [[]]:
        return 1
    elif len1 != len2:
        raise ValueError("matrix must be a square matrix")
    if len1 == 1 and len2 == 0:
        return 1
    if len1 == 1 and len2 == 1:
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
