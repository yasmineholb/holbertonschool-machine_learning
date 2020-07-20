#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
plt.ylabel('Number of Students')
plt.xlabel('Grades')
plt.title('Project A')
plt.axis([0 ,100, 0, 30])
x = np.arange(0, 110, 10)
bn = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(student_grades, edgecolor="black", bins = bn)
plt.xticks(x)
plt.show()
