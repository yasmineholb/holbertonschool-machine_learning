#!/usr/bin/env python3
""" pooling function """
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """ Function that performs pooling on images """
    m, h, w, c = np.shape(images)
    kh, kw = kernel_shape
    sh, sw = stride
    t = np.arange(m)
    h1 = int((h-kh)/sh) + 1
    w1 = int((w-kw)/sw) + 1
    output = np.zeros((m, h1, w1, c))
    for x in range(h1):
        for y in range(w1):
            if mode == 'max':
                output[t, x, y] = np.max(images[t,
                                                x*sh:(kh+(x*sh)),
                                                y*sw:(kw+(y*sw))], axis=(1, 2))
            else:
                output[t, x, y] = np.mean(images[t,
                                                 x*sh:(kh+(x*sh)),
                                                 y*sw:(kw+(y*sw))],
                                          axis=(1, 2))
    return output
