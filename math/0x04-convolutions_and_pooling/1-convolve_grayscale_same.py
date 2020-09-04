#!/usr/bin/env python3
""" convolve function """
import numpy as np


def convolve_grayscale_same(images, kernel):
    """ Function that performs a same
        convolution on grayscale images """
    m, h, w = np.shape(images)
    kh, kw = np.shape(kernel)
    image = np.zeros((m, h + kh - 1, w + kw - 1))
    if kh % 2 == 1:
        ph = (kh-1)//2
    else:
        ph = kh//2
    if kw % 2 == 1:
        pw = (kw-1)//2
    else:
        pw = kw//2
    image[:, ph:h+ph, pw:w+pw] = images.copy()
    S = np.zeros((m, h, w))
    im = np.arange(0, m)
    for i in range(h):
        for j in range(w):
            S[im, i, j] = np.sum(image[im, i:i + kh, j:j + kw] * kernel,
                                 axis=(1, 2))
    return S
