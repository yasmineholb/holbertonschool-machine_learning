#!/usr/bin/env python3
""" new fn """


def matrix_shape(matrix):
    """ matrix shappe """
    lis = [len(matrix)]
    while(type(matrix[0]) == list):
        lis.append(len(matrix[0]))
        matrix = matrix[0]
    return(lis)
