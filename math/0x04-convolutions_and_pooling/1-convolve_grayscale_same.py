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
    pad_along_height = max((output_h - 1) + kh - h, 0)
    pad_along_width = max((output_w - 1) + kw - w, 0)
    pad_top = pad_along_height // 2             # amount of zero padding on the top
    pad_bottom = pad_along_height - pad_top     # amount of zero padding on the bottom
    pad_left = pad_along_width // 2             # amount of zero padding on the left
    pad_right = pad_along_width - pad_left      # amount of zero padding on the right
    output = np.zeros((m, output_h, output_w))  # convolution output
    # Add zero padding to the input image
    image_padded = np.zeros((m, h + pad_along_height,
                            w + pad_along_width))
    """image_padded[m, pad_top:-pad_bottom, pad_left:-pad_right, :] = conv_input"""
    for x in range(output_h):
        for y in range(output_w):
            output[t, x, y] = (image_padded[t, x:kh+x, y:kw+y] * kernel).sum(
                axis=(1, 2)) 
    return output
