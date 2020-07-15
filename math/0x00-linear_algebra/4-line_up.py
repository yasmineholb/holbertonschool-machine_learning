#!/usr/bin/env python3
""" add array"""


def add_arrays(arr1, arr2):
    """ add fn"""
    s = []
    if len(arr1) != len(arr2):
        return(None)
    else:
        for i in range(len(arr1)):
            s.append(arr1[i] + arr2[i])
    return(s)
