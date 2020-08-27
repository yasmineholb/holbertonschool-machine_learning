#!/usr/bin/env python3
""" l2 regularization function """
import numpy as np


def l2_reg_cost(cost):
    """ function that calculates the cost of
        a neural network with L2 regularization """
    return tf.losses.get_regularization_loss() + cost
