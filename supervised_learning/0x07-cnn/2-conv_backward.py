#!/usr/bin/env python3
""" convolution backward Prop """
import numpy as np


def conv_backward(dZ, A_prev, W, b, padding="same", stride=(1, 1)):
    """
    Implement the backward propagation for a convolution function
    """
    """
    parametres
    """
    m, h_new, w_new, c_new = dZ.shape
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, c_prev, c_new = W.shape
    sh, sw = stride
    """
    initialisation
    """
    dA_prev = np.zeros((m, h_prev, w_prev, c_prev))
    dW = np.zeros((kh, kw, c_prev, c_new))
    db = np.zeros((1, 1, 1, c_new))
    """
    padding parametres
    """
    if padding == "valid":
        ph = 0
        pw = 0
    elif padding == "same":
        ph = int(((h_prev - 1) * sh + kh - kh % 2 - h_prev) / 2) + 1
        pw = int(((w_prev - 1) * sw + kw - kw % 2 - w_prev) / 2) + 1
    else:
        ph, pw = padding
    """
    padding
    """
    A_prev_pad = np.zeros((m, (h_prev + 2 * ph), (w_prev + 2 * pw), c_prev))
    A_prev_pad[:, ph:h_prev + ph, pw:w_prev + pw, :] = A_prev.copy()
    dA_prev_pad = np.zeros((m, (h_prev + 2 * ph), (w_prev + 2 * pw), c_prev))
    """
    Loop
    """
    for i in range(m):
        a_prev_pad = A_prev_pad[i]
        da_prev_pad = dA_prev_pad[i]
        for h in range(h_new):
            for w in range(w_new):
                for c in range(c_new):
                    """
                    Slicing
                    """
                    vert_start = h * stride[0]
                    vert_end = vert_start + kh
                    horiz_start = w * stride[1]
                    horiz_end = horiz_start + kw
                    a_slice = a_prev_pad[vert_start:vert_end,
                                         horiz_start:horiz_end, :]
                    """
                    backwarding
                    """
                    da_prev_pad[vert_start:vert_end,
                                horiz_start:horiz_end,
                                :] += W[:, :, :, c] * dZ[i, h, w, c]
                    dW[:, :, :, c] += a_slice * dZ[i, h, w, c]
                    db[:, :, :, c] += dZ[i, h, w, c]
        """
        dA without padding
        """
        dA_prev[i, :, :, :] = da_prev_pad[ph:h_prev + ph, pw: w_prev + pw, :]
    return dA_prev, dW, db
