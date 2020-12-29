#!/usr/bin/env python3
""" Unigram BLEU score """
import numpy as np


def uni_bleu(references, sentence):
    """ function that calculates the
        unigram BLEU score for a sentence """
    sen = list(set(sentence))
    dictt = {}
    for ref in references:
        for r in ref:
            if r in sen:
                if r not in dictt.keys():
                    dictt[r] = ref.count(r)
                else:
                    m = ref.count(r)
                    n = dictt[r]
                    dictt[r] = max(m, n)
    lenn = len(sentence)
    lrefs = []
    for ref in references:
        lenr = len(ref)
        lrefs.append(((abs(lenr - lenn)), lenr))
    refl = sorted(lrefs, key=lambda x: x[0])
    refl = refl[0][1]
    if lenn > refl:
        bp = 1
    else:
        bp = np.exp(1 - (float(refl) / lenn))
    Bleu_score = bp * np.exp(np.log(sum(dictt.values()) / lenn))
    return Bleu_score
