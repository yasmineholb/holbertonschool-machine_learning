#!/usr/bin/env python3
""" slice  function"""
import numpy as np
import matplotlib.pyplot as plt


y = np.arange(0, 11) ** 3
plt.plot(y, 'red')
plt.xlim([0, 10])
plt.show()
