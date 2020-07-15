#!/usr/bin/env python3
def matrix_shape(matrix):
    lis = [len(matrix)]
    while(type(matrix[0]) == list):
        lis.append(len(matrix[0]))
        matrix = matrix[0]
    return(lis)
