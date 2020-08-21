#!/usr/bin/env python3
""" norm constatnts """
import numpy as np


def normalize(X, m, s):
    """ normalize function """
    X = X - m
    X = X / s
    return X
