#!/usr/bin/env python3
""" convolve function """
import numpy as np


def convolve_grayscale(images, kernel, padding='same',
                       stride=(1, 1)):
    """ Function that that performs a convolution on
        grayscale images """
    m, h, w = np.shape(images)
    kh, kw = np.shape(kernel)
    if padding == "valid":
        ph = 0
        pw = 0
    elif padding == "same":
        if kh % 2 == 1:
            ph = (kh-1)//2
        else:
            ph = kh//2
        if kw % 2 == 1:
            pw = (kw-1)//2
        else:
            pw = kw//2
    else:
        ph, pw = padding
    sh, sw = stride
    image = np.zeros((m, (h + 2 * ph), (w + 2 * pw)))
    image[:, ph:h+ph, pw:w+pw] = images.copy()
    t1, h1, w1 = np.shape(image)
    S = np.zeros((m, ((h + 2 * ph - kh) // stride[0]) + 1,
                  ((w + 2 * pw - kw) // stride[1]) + 1))
    im = np.arange(0, m)
    for i in range(((h + 2 * ph - kh) // stride[0]) + 1):
        for j in range(((w + 2 * pw - kw) // stride[1]) + 1):
            S[im, i, j] = np.sum(image[im,
                                       sh * i:sh * i + kh,
                                       sw * j:sw * j + kw] * kernel,
                                 axis=(1, 2))
    return S
