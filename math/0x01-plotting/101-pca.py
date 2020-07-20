#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]
data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(pca_data[:, 0], pca_data[:, 1], pca_data[:, 2],c=labels, cmap='plasma', edgecolor='face', s=40)
ax.set_title("PCA of Iris Dataset")
ax.set_xlabel("U1")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("U2")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("U3")
ax.w_zaxis.set_ticklabels([])
plt.show()
