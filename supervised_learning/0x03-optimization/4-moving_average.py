#!/usr/bin/env python3
""" Moiving Average """

"""Ressources à regarder:
    https://www.youtube.com/watch?v=lAq96T8FkTw
    https://www.youtube.com/watch?v=lWzo8CajF5s"""


def moving_average(data, beta):
    """ Moiving Average """
    V = [0]
    W = []
    for i in range(len(data)):
        V.append((1 - beta) * data[i] + beta * V[i])
        W.append(V[i+1] / (1 - beta ** (i+1)))
    return W
