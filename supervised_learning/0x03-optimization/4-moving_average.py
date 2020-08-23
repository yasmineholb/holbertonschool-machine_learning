#!/usr/bin/env python3
""" Moving Average"""
import numpy as np

"""Ressources à regarder:
    https://www.youtube.com/watch?v=lAq96T8FkTw
    https://www.youtube.com/watch?v=lWzo8CajF5s"""


def moving_average(data, beta):
    """ Moving Average"""
    V = [0]
    for i in range(len(data)):
        V.append((1 - beta) * data[i] + beta * V[i])
    V = np.asarray(V[1:])/np.asarray([1-beta**(i+1) for i in range(len(data))])
    return V
