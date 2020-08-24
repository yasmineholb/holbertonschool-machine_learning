#!/usr/bin/env python3
""" f1 score """
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """ calculate f1 score """
    pres = precision(confusion)
    sen = sensitivity(confusion)
    f1 = 2 * (pres*sen) / (pres+sen)
    return f1
