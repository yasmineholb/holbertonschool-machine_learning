#!/usr/bin/env python3
""" convolve function """
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """ Function that performs a valid
        convolution on grayscale images """
    m, h, w = np.shape(images)
    kh, kw = np.shape(kernel)
    output_h = h - kh + 1
    output_w = w - kw + 1
    t = np.arange(m)
    output = np.zeros((m, output_h, output_w))
    for x in range(output_h):
        for y in range(output_w):
            output[t, x, y] = (images[t, x:kh+x, y:kw+y] * kernel).sum(
                axis=(1, 2))
    return output
