#!/usr/bin/env python3
""" Pooling Forward Prop """
import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1),
                 mode='max'):
    """ Function that performs forward propagation over
        a pooling layer of a neural network """
    m, h_prev, w_prev, c_prev = np.shape(A_prev)
    kh, kw = kernel_shape
    sh, sw = stride
    t = np.arange(m)
    h1 = int((h_prev-kh)/sh) + 1
    w1 = int((w_prev-kw)/sw) + 1
    output = np.zeros((m, h1, w1, c_prev))
    for x in range(h1):
        for y in range(w1):
            if mode == 'max':
                output[t, x, y] = np.max(A_prev[t,
                                                x*sh:(kh+(x*sh)),
                                                y*sw:(kw+(y*sw))], axis=(1, 2))
            else:
                output[t, x, y] = np.mean(A_prev[t,
                                                 x*sh:(kh+(x*sh)),
                                                 y*sw:(kw+(y*sw))],
                                          axis=(1, 2))
    return output
