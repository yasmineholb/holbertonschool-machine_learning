#!/usr/bin/env python3
""" convolve function """
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """ Function that performs a convolution on grayscale
        images with custom padding """
    m, h, w = np.shape(images)
    kh, kw = np.shape(kernel)
    ph = (padding[0] - padding[0] % 2) // 2
    pw = (padding[1] - padding[1] % 2) // 2
    image = np.zeros((m, h + padding[0], w + padding[1]))
    image[:, ph:h+ph, pw:w+pw] = images.copy()
    t1, h1, w1 = np.shape(image)
    S = np.zeros((m, h1 - kh + 1, w1 - kw + 1))
    im = np.arange(0, m)
    for i in range(h1 - kh + 1):
        for j in range(w1 - kw + 1):
            S[im, i, j] = np.sum(image[im, i:i + kh, j:j + kw] * kernel,
                                 axis=(1, 2))
    return S
