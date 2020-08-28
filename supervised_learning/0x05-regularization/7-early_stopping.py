#!/usr/bin/env python3
""" early stopping function """


def early_stopping(cost, opt_cost, threshold, patience, count):
    """ that determines if you should stop gradient
        descent early """
    if opt_cost <= cost + threshold:
        count = count + 1
    else:
        count = 0
    if count >= patience:
        return True, count
    else:
        return False, count
