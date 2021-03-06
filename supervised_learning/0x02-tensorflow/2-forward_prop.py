#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def forward_prop(x, layer_sizes=[], activations=[]):
    """ forward prop """
    create_layer = __import__('1-create_layer').create_layer
    prev = x
    for i in range(len(layer_sizes)):
        prev = create_layer(prev, layer_sizes[i], activations[i])
        """prev2 = create_layer(prev1, layer_sizes[1], activations[1])
        prev3 = create_layer(prev2, layer_sizes[2], activations[2])"""
    return prev
