#!/usr/bin/env python3
""" convolve function """
import numpy as np


def convolve_grayscale_same(images, kernel):
    """ Function that performs a same
        convolution on grayscale images """
    m, h, w = np.shape(images)
    kh, kw = np.shape(kernel)
    output_h = h - kh + 1
    output_w = w - kw + 1
    t = np.arange(m)
    output = np.zeros((m, output_h, output_w))
    image_padded = np.zeros((m, (h + (kh-1)), 
                             (w + (kw-1))))   
    image_padded[t, (kh//2):-(kh//2), 
                 (kw//2):-(kw//2)] = images
    """image_padded[m, pad_top:-pad_bottom, pad_left:-pad_right, :] = conv_input"""
    for x in range(output_h):
        for y in range(output_w):
            output[t, x, y] = (image_padded[t, x:kh+x, y:kw+y] * kernel).sum(
                axis=(1, 2)) 
    return output
