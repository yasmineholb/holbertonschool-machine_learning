#!/usr/bin/env python3
""" slice  function"""
import numpy as np
import matplotlib.pyplot as plt


mean = [69, 0]
cov = [[15, 8], [8, 5]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

plt.ylabel('Weight (lbs)')
plt.xlabel('Height (in)')
plt.title('Men\'s Height vs Weight')
plt.plot(x, y, 'm.')
plt.show()

