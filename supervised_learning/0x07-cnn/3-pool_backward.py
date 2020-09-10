#!/usr/bin/env python3
""" Pooling backward Prop """
import numpy as np


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """ Function that performs backward propagation over
        a pooling layer of a neural network """
    m, h_new, w_new, c_new = dA.shape
    m, h_prev, w_prev, c = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    dA_prev = np.zeros(A_prev.shape)
    
    for i in range(m):                       
        a_prev = A_prev[i]
        for h in range(h_new):                   
            for w in range(w_new):               
                for c in range(c_new):   
                    
                    h_start  = h * sh
                    h_end    = (h * sh) + kh
                    w_start = w * sw
                    w_end   = (w * sw) + kw
                    
                    if mode == "max":
                        a_prev_slice = a_prev[h_start:h_end, w_start:w_end, c]
                        mask = (a_prev_slice == np.max(a_prev_slice))
                        dA_prev[i, h_start:h_end, w_start:w_end, c] += mask * dA[i, h, w, c]
                    
                    elif mode == "average":
                        da = dA[i, h, w, c]
                        shape = (kh, kw)
                        average = da / (kh * kw) * np.ones(shape)
                        dA_prev[i, h_start:h_end, w_start:w_end, c] += average
    return dA_prev
