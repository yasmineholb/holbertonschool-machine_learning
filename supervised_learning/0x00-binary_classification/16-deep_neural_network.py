#!/usr/bin/env python3
""" new class """
import numpy as np


class DeepNeuralNetwork():
    """ DeepNeuralNetwork class"""
    def __init__(self, nx, layers):
        """ init function """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list:
            raise TypeError("layers must be a list of positive integers")
        for i in layers:
            if type(i) is not int:
                raise TypeError("layers must be a list of positive integers")
        self.L = layers[0]
        self.cache = {}
        self.weights = 
