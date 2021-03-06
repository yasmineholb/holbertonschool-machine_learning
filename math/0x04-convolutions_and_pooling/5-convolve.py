#!/usr/bin/env python3
""" convolve function """
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """ Function that that performs a convolution on
        channels """
    m, h, w, c = np.shape(images)
    kh, kw, c, nc = np.shape(kernels)
    sh, sw = stride
    if padding == "valid":
        ph = 0
        pw = 0
    elif padding == "same":
        ph = int(((h - 1) * sh + kh - h) / 2) + 1
        pw = int(((w - 1) * sw + kw - w) / 2) + 1
    else:
        ph, pw = padding
    image = np.zeros((m, (h + 2 * ph), (w + 2 * pw), c))
    image[:, ph:h+ph, pw:w+pw, :] = images.copy()
    nh = np.floor(((h + 2 * ph - kh) / stride[0]) + 1).astype(int)
    nw = np.floor(((w + 2 * pw - kw) / stride[1]) + 1).astype(int)
    S = np.zeros((m, nh, nw, nc))
    im = np.arange(0, m)
    for i in range(nh):
        for j in range(nw):
            for k in range(nc):
                S[im, i, j, k] += np.sum(image[im, sh * i:sh * i + kh,
                                               sw * j:sw * j + kw, :]
                                         * kernels[:, :, :, k],
                                         axis=(1, 2, 3))
    return S
