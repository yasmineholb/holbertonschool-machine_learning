#!/usr/bin/env python3
""" save conf """
import tensorflow.keras as K


def save_config(network, filename):
    """ Function that saves a model’s
        configuration in JSON format """
    with open(filename, "w") as fl:
        fl.write(network.to_json())
    return None


def load_config(filename):
    """ Function that loads
        a model with a specific
        configuration: """
    with open(filename, "r") as fl:
        read_f = fl.read()
    ld = K.models.model_from_json(read_f)
    return ld
